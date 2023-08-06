"""
This module supports to generate additional features for HANA DataFrame.
"""
from hana_ml import dataframe
from hana_ml.dataframe import quotename

#pylint: disable=invalid-name
#pylint: disable=eval-used
#pylint: disable=unused-variable
#pylint: disable=line-too-long
#pylint: disable=too-many-arguments
#pylint: disable=too-many-locals
#pylint: disable=too-many-branches
#pylint: disable=too-many-nested-blocks

def generate_feature(data,
                     targets,
                     group_by=None,
                     agg_func=None,
                     trans_func=None,
                     order_by=None,
                     trans_param=None,
                     ):
    """
    Add additional features to the existing dataframe using agg_func and trans_func.

    Parameters
    ----------
    data : DataFrame
        SAP HANA DataFrame.
    targets : str or list of str
        The column(s) in data to be feature engineered.
    group_by : str, optional
        The column in data for group by when performing agg_func.
    agg_func : str, optional
        HANA aggeration operations. SUM, COUNT, MIN, MAX, ...
    trans_func : str, optional
        HANA transformation operations. MONTH, YEAR, LAG, ...
    order_by : str, optional
        LEAD, LAG function requires an OVER(ORDER_BY) window specification.
    trans_param : list, optional
        Parameters for transformation operations corresponding to targets.
    Returns
    -------

    DataFrame
        SAP HANA DataFrame with new features.

    Examples
    --------

    >>> df.head(5).collect()
                  TIME        TEMPERATURE    HUMIDITY      OXYGEN          CO2
        0   2021-01-01 12:00:00 19.972199   29.271170   23.154523   504.806395
        1   2021-01-01 12:00:10 19.910014   27.931855   23.009835   507.515937
        2   2021-01-01 12:00:20 19.834676   26.051309   22.756407   510.111974
        3   2021-01-01 12:00:30 19.952517   26.007655   22.737376   516.993696
        4   2021-01-01 12:00:40 20.163497   26.056979   22.469276   528.337481
    >>> generate_feature(data=df,
                         targets=["TEMPERATURE", "HUMIDITY", "OXYGEN", "CO2"],
                         trans_func="LAG",
                         order_by="TIME",
                         trans_param=[range(1, 7), range(1, 5), range(1, 5), range(1,7)]).dropna().deselect("TIME").head(2).collect()
      TEMPERATURE     HUMIDITY     OXYGEN          CO2 LAG(TEMPERATURE, 1)  ...  LAG(CO2, 4)
     0  20.978001   26.187823   21.982030   522.731895           20.701740  ...  510.111974
     1  21.234148   25.703989   21.804864   528.066402           20.978001  ...  516.993696
    """
    view_sql = data.select_statement
    if not isinstance(targets, (tuple, list)):
        targets = [targets]
    dummy_list = range(2, 2+len(targets))
    if agg_func is not None:
        if group_by is None:
            raise Exception("group_by cannot be None!")
        agg_keyword_list = ['"{}({})"'.format(agg_func, target) for target in targets]
        agg_sql_list = ["SELECT {}, {}({}) {} FROM ({}) GROUP BY {}".format(quotename(group_by),\
             agg_func, quotename(target), agg_keyword, view_sql, quotename(group_by))\
             for target, agg_keyword in zip(targets, agg_keyword_list)]
        view_sql_select = "SELECT T1.* "
        view_sql_join = ""
        for agg_sql, agg_keyword, dummy in zip(agg_sql_list, agg_keyword_list, dummy_list):
            view_sql_select += ", T{}.{} ".format(dummy, agg_keyword)
            view_sql_join += "INNER JOIN ({1}) T{0} ON T1.{2}=T{0}.{2} ".format(dummy, agg_sql,\
                 quotename(group_by))
        view_sql = view_sql_select + "FROM ({}) T1 ".format(view_sql) + view_sql_join

    if not isinstance(trans_param, (tuple, list)):
        if trans_param is not None:
            trans_param = [trans_param]

    trans_keyword_list = []
    if trans_func is not None:
        if trans_param is not None:
            for target, param in zip(targets, trans_param):
                if isinstance(param, (tuple, list, range)):
                    for t_param in param:
                        temp_param = t_param
                        if isinstance(t_param, (tuple, list)):
                            temp_param = ', '.join(t_param)
                        temp_trans = '{}({}, {})'.format(trans_func, quotename(target), temp_param)
                        if order_by is not None:
                            temp_trans = temp_trans + ' OVER(ORDER BY {}) AS "{}" '.format(quotename(order_by), temp_trans.replace('"', ''))
                        else:
                            temp_trans = temp_trans + ' AS "{}"'.format(temp_trans.replace('"', ''))
                        trans_keyword_list.append(temp_trans)
                else:
                    temp_trans = '{}({}, {})'.format(trans_func, quotename(target), param)
                    if order_by is not None:
                        temp_trans = temp_trans + ' OVER(ORDER BY {}) AS "{}" '.format(quotename(order_by), temp_trans.replace('"', ''))
                    else:
                        temp_trans = temp_trans + ' AS "{}"'.format(temp_trans.replace('"', ''))
                    trans_keyword_list.append(temp_trans)
        else:
            for target in targets:
                temp_trans = '{}({})'.format(trans_func, quotename(target))
                if order_by is not None:
                    temp_trans = temp_trans + ' OVER(ORDER BY {}) AS "{}" '.format(quotename(order_by), temp_trans.replace('"', ''))
                else:
                    temp_trans = temp_trans + ' AS "{}"'.format(temp_trans.replace('"', ''))
                trans_keyword_list.append(temp_trans)

        view_sql = "SELECT *, " + ", ".join(trans_keyword_list) + " FROM ({})".format(view_sql)
    return dataframe.DataFrame(data.connection_context, view_sql)

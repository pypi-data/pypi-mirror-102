"""
This module contains factory functions to create Graph objects based
on different inputs.

The following functions are available:

* :func: `create_hana_graph_from_vertex_and_edge_frames`
* :func: `create_hana_graph_from_existing_workspace`
"""

# pylint: disable=bad-continuation
# pylint: disable=too-many-locals
# pylint: disable=too-many-arguments
# pylint: disable=too-many-branches
# pylint: disable=invalid-name
# pylint: disable=too-many-lines
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-statements

import logging

import numpy as np
import pandas as pd
from hdbcli import dbapi

from hana_ml import DataFrame
from hana_ml.dataframe import create_dataframe_from_pandas
from .constants import EDGE_ID
from .discovery import discover_graph_workspaces

logger = logging.getLogger(__name__)


def create_hana_graph_from_vertex_and_edge_frames(
    connection_context,
    vertices_hdf,
    edges_hdf,
    workspace_name,
    schema=None,
    edge_source_column="from",
    edge_target_column="to",
    edge_key_column=None,
    vertex_key_column=None,
    object_type_as_bin=False,
    drop_exist_tab=True,
    force=True,
    replace=True,
    geo_cols=None,
    srid=None,
):
    """
    Expects either a hana dataframe or pandas dataframe as input for each
    vertex and edges table, thus the function expects an n_frame and e_frame.
    If it is pandas then it will be transformed into a hana_ml.DataFrame.

    If it is an hdf then the graph only needs to be created by combining
    existing tables. No collecting.
    If it is a pdf then the tables expect to need to be created and then
    the gws from those resulting tables.
    If it is just an edge list then the graph workspace needs to be
    created from a notional vertices table and the edge content.

    Parameters
    ----------
    connection_context : ConnectionContext
        The connection to the SAP HANA system.
    vertices_hdf : pandas.DataFrame or hana_ml.DataFrame
        Table of data containing vertices and their keys that correspond
        with the edge frame.
    edges_hdf : pandas.DataFrame or hana_ml.DataFrame
        Table of data containing edges that link keys within the vertex frame.
    workspace_name : str
        Name of the workspace expected in the SAP HANA Graph workspaces
        of the ConnectionContext.
    schema : str
        Schema name of the workspace.

        Defaults to ConnectionContext current_schema.
    edge_source_column : str
        Column name in the e_frame containing only source vertex keys that
        exist within the vertex_key_column of the n_frame.

        Defaults to 'from'.
    edge_target_column : str
        Column name in the e_frame containing the unique id of the edge.

        Defaults to 'to'.
    edge_key_column : str
        Column name in the n_frame containing the vertex key which uniquely
        identifies the vertex in the edge table.

        Defaults to None.
    vertex_key_column : str
        Column name in the n_frame containing the vertex key which uniquely
        identifies the vertex in the edge table.

        Defaults to None.
    object_type_as_bin : bool, optional
        If True, the object type will be considered CLOB in SAP HANA.

        Defaults to False.
    drop_exist_tab : bool, optional
        If force is True, drop the existing table when drop_exist_tab is
        True and truncate the existing table when it is
        False.

        Defaults to False.
    force : bool, optional
        If force is True, then the SAP HANA table with table_name is
        truncated or dropped.

        Defaults to False.
    replace : bool, optional
        If replace is True, then the SAP HANA table performs the missing
        value handling.

        Defaults to True.
    geo_cols : dict, (optional but required for Spatial functions)
        Tuples or strings as keys that denote columns with geometric data and srid as values.

        Defaults to None.

    srid : int, (optional for Spatial functions)
        Spatial reference system id.

        Defaults to None.

    Returns
    -------
    Graph
        A virtual HANA Graph with functions inherited from the individual
        vertex and edge HANA Dataframes.

    Examples
    --------
    >>> n_path = os.path.join(self.datasets, 'nodes.csv')
    >>> e_path = os.path.join(self.datasets, 'edges.csv')
    >>> vertex_key_column = 'guid'
    >>> edge_from_col = 'from'
    >>> edge_to_col = 'to'
    >>> edge_label = 'label'
    >>> nodes = pd.read_csv(n_path)
    >>> edges = pd.read_csv(e_path)
    >>> # Create the hana_graph based on the 2 csv
    >>> hana_graph = create_hana_graph_from_vertex_and_edge_frames(
    >>> ... connection_context=ConnectionContext(), vertices_hdf=nodes,
    >>> ... edges_hdf=edges, workspace_name=workspace_name,
    >>> ... schema='SYSTEM', vertex_key_column=vertex_key_column,
    >>> ... edge_source_column=edge_from_col, edge_target_column=edge_to_col,
    >>> ... object_type_as_bin=False, drop_exist_tab=True)

    """
    if not schema:
        schema = connection_context.get_current_schema()

    if isinstance(vertices_hdf, pd.DataFrame) and isinstance(edges_hdf, pd.DataFrame):
        # Use the 2 pandas dataframes as vertex and edges tables to create a workspace
        # and return the collect statements
        vertex_table_name = "{}_VERTICES".format(workspace_name)
        edge_table_name = "{}_EDGES".format(workspace_name)

        # Check geo_cols and whether it references a column in the node or edges table
        if isinstance(geo_cols, list):
            if srid:
                geo_cols = {col: srid for col in geo_cols}
            else:
                raise ValueError("SRID required if sending a list of columns")

        if isinstance(geo_cols, dict):
            v_geo_cols = {
                col: geo_cols[col] for col in geo_cols if col in vertices_hdf.columns
            }
            e_geo_cols = {
                col: geo_cols[col] for col in geo_cols if col in edges_hdf.columns
            }

        elif geo_cols is None:
            v_geo_cols = None
            e_geo_cols = None

        else:
            raise TypeError(
                "Geometry provided was a {} when a dict or list is expected".format(
                    type(geo_cols)
                )
            )

        vertices = create_dataframe_from_pandas(
            connection_context,
            pandas_df=vertices_hdf,
            schema=schema,
            replace=replace,
            force=force,
            table_name=vertex_table_name,
            object_type_as_bin=object_type_as_bin,
            drop_exist_tab=drop_exist_tab,
            primary_key=vertex_key_column,
            geo_cols=v_geo_cols,
        )

        # If there is no edge_col_key then assign one called EDGE_ID and base
        # values on a row sequence for id
        if not edge_key_column:
            edge_key_column = EDGE_ID
            edges_hdf.insert(loc=0, column=EDGE_ID, value=np.arange(len(edges_hdf)))

        # Create the Edge table within the same schema but not as its own Dataframe
        edges = create_dataframe_from_pandas(
            connection_context,
            pandas_df=edges_hdf,
            schema=schema,
            table_name=edge_table_name,
            geo_cols=e_geo_cols,
            force=force,
            drop_exist_tab=drop_exist_tab,
            replace=replace,
            primary_key=edge_key_column,
            not_nulls=[edge_key_column, edge_source_column, edge_target_column],
        )

    elif isinstance(edges_hdf, pd.DataFrame):
        logger.info("Creating graph only from edge list not available yet")
        raise ValueError("Creating graph only from edge list not available yet")

    elif isinstance(vertices_hdf, DataFrame) and isinstance(edges_hdf, DataFrame):
        # Create a view on the HANA Dataframes to prevent any unintended changes
        # to source tables
        vertex_table_name = "{}_VIEW".format(vertices_hdf.source_table["TABLE_NAME"])
        edge_table_name = "{}_VIEW".format(edges_hdf.source_table["TABLE_NAME"])

        try:
            connection_context.connection.cursor().execute(
                "DROP VIEW {};".format(vertex_table_name)
            )
        except dbapi.Error:
            pass

        try:
            connection_context.connection.cursor().execute(
                "DROP VIEW {};".format(edge_table_name)
            )
        except dbapi.Error:
            pass

        vertices = vertices_hdf.save(
            where=vertex_table_name, table_type="VIEW", force=True
        )
        vertices.geo_cols = vertices_hdf.geo_cols
        edges = edges_hdf.save(where=edge_table_name, table_type="VIEW", force=True)
        edges.geo_cols = edges_hdf.geo_cols

    else:
        raise ValueError("An edges and vertices definition are required.")

    # Import the Graph Object here, to avoid circular dependencies
    from .hana_graph import Graph  # pylint: disable=import-outside-toplevel

    hana_graph = Graph(
        connection_context=connection_context,
        schema=schema,
        vertices_hdf=vertices,
        edges_hdf=edges,
        vertex_tbl_name=vertex_table_name,
        edge_tbl_name=edge_table_name,
        vertex_key_column=vertex_key_column,
        edge_key_column=edge_key_column,
        edge_source_column=edge_source_column,
        edge_target_column=edge_target_column,
        workspace_name=workspace_name,
    )

    return hana_graph


def create_hana_graph_from_existing_workspace(
    connection_context, workspace_name, schema=None
):
    """
    Given a workspace name that is assumed to exist within the
    connection_context, return a Graph as if created from
    external data sources.

    Parameters
    ----------
    connection_context : ConnectionContext
        The connection to the SAP HANA system.
    workspace_name : str
        Case sensitive name of the HANA Graph workspace.
    schema : str, optional
        Schema name of the workspace.

        Defaults to ConnectionContext current_schema.

    Returns
    -------
    Graph
        A virtual HANA Graph with functions inherited from the individual
        vertex and edge HANA Dataframes.

    """
    if not schema:
        schema = connection_context.get_current_schema()

    # Get the workspaces in the given connection context and ensure the
    # named space is included.
    summary = discover_graph_workspaces(connection_context)

    meta = [
        graph
        for index, graph in summary.iterrows()
        if graph["WORKSPACE_NAME"] == workspace_name
    ]

    if len(meta) < 1:
        raise ValueError("No graph workspace found with name {}".format(workspace_name))

    else:
        meta = meta[0]
        vertex_table_reference = '"{}"."{}"'.format(
            meta["VERTEX_SCHEMA_NAME"], meta["VERTEX_TABLE_NAME"]
        )

        edge_table_reference = '"{}"."{}"'.format(
            meta["EDGE_SCHEMA_NAME"], meta["EDGE_TABLE_NAME"]
        )

        # Import the Graph Object here, to avoid circular dependencies
        from .hana_graph import Graph  # pylint: disable=import-outside-toplevel

        hana_graph = Graph(
            connection_context=connection_context,
            schema=schema,
            vertices_hdf=DataFrame(
                connection_context,
                select_statement="SELECT * FROM {}".format(vertex_table_reference),
            ),
            edges_hdf=DataFrame(
                connection_context,
                select_statement="SELECT * FROM {}".format(edge_table_reference),
            ),
            vertex_tbl_name=meta["VERTEX_TABLE_NAME"],
            edge_tbl_name=meta["EDGE_TABLE_NAME"],
            vertex_key_column=meta["VERTEX_KEY_COLUMN_NAME"],
            edge_key_column=meta["EDGE_KEY_COLUMN_NAME"],
            edge_source_column=meta["EDGE_SOURCE_COLUMN_NAME"],
            edge_target_column=meta["EDGE_TARGET_COLUMN"],
            workspace_name=meta["WORKSPACE_NAME"],
        )

        return hana_graph

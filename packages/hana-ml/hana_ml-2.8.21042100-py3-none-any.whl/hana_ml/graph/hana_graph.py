"""
This module represents a database set of HANA Dataframes that are
the edge and vertex tables of a HANA Graph.

The following classes and functions are available:

    * :class:`Graph`
    * :class:`Path`
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

import pandas as pd
from hdbcli import dbapi

from .constants import (
    DIRECTIONS,
    DEFAULT_DIRECTION,
    DIRECTION_INCOMING,
    DIRECTION_OUTGOING,
    DIRECTION_ANY,
)

logger = logging.getLogger(__name__)


class Path(object):
    """
    Represents a group of vertices and edges that define a path. Used by
    the Graph object when running functions that return more than a single
    set of values. Prevents the user from requiring verbose syntax to access
    results. For example, returning a dictionary from the functions would
    require a user to write path['edges'] instead of path.edges().

    Parameters
    ----------
    edges : pd.DataFrame
        Path defined by a collection of source and target columns with
        vertex keys values expected in those columns.

    vertices : pd.DataFrame
        Vertices that are included in the path.

    """

    def __init__(self, edges: pd.DataFrame, vertices: pd.DataFrame, weight=None):
        self.edge_table = edges
        self.vertex_table = vertices
        self._weight = weight

    def edges(self) -> pd.DataFrame:
        """

        Returns
        -------
        Pandas Dataframe containing the edges.

        """
        return self.edge_table

    def vertices(self) -> pd.DataFrame:
        """

        Returns
        -------
        Pandas Dataframe containing the vertices.

        """
        return self.vertex_table

    def weight(self):
        """

        Returns
        -------
        float

        """
        return self._weight


class Graph(object):  # pylint: disable=too-many-public-methods
    """
    Represents a graph consisting of a vertex and edges table that was
    created from a set of pandas dataframes, existing tables that are
    changed into a graph workspace, or through an existing graph workspace.

    Parameters
    ----------
    connection_context : ConnectionContext
        The connection to the SAP HANA system.
    schema : str
        Name of the schema.
    vertices_hdf : hana_ml.Dataframe
        Table object representing vertices derived from a set of tables.
    edges_hdf : hana_ml.Dataframe
        Table object representing edges derived from a set of tables.
    vertex_tbl_name : str
        Name that references the source table for vertices.
    edge_tbl_name : str
        Name that references the source table for edges.
    vertex_key_column : str
        Name of the column containing the unique identifier for
        nodes/vertices.
    edge_key_column : str
        Name of the column containing the unique identifier for
        edges/links.
    edge_source_column : str
        Name that references the column where the keys for the source in
        an edge are located.
    edge_target_column : str
        Name that references the column where the keys for the target in
        an edge are located.
    workspace_name : str
        Name that references the HANA Graph workspace.
    """

    def __init__(
        self,
        connection_context,
        schema,
        vertices_hdf,
        edges_hdf,
        vertex_tbl_name,
        edge_tbl_name,
        vertex_key_column,
        edge_key_column,
        edge_source_column,
        edge_target_column,
        workspace_name,
    ):

        self.connection_context = connection_context
        self.schema = schema
        self.vertices_hdf = vertices_hdf
        self.edges_hdf = edges_hdf
        self.vertex_tbl_name = vertex_tbl_name
        self.edge_tbl_name = edge_tbl_name
        self.vertex_key_column = vertex_key_column

        vertex_dt = [
            dtype[1]
            for dtype in self.vertices_hdf.dtypes()
            if dtype[0] == self.vertex_key_column
        ][0]
        if vertex_dt == "NVARCHAR":
            vertex_dt = "NVARCHAR(5000)"
        self.vertex_key_col_dtype = vertex_dt

        self.edge_key_column = edge_key_column
        self.edge_source_column = edge_source_column
        self.edge_target_column = edge_target_column
        self.workspace_name = workspace_name
        self._create_graph()

    def _vertex_columns(self):
        _cols = []

        for dtype in self.vertices_hdf.dtypes():
            if dtype[0] == self.vertex_key_column:
                if dtype[1].upper() == "NVARCHAR":
                    _cols.append('"{}" {}(5000)'.format(dtype[0], dtype[1].upper()))
                else:
                    _cols.append('"{}" {}'.format(dtype[0], dtype[1].upper()))

        return ", ".join(_cols)

    def _edge_columns(self, valid_edge):
        _cols = []

        ", ".join(
            [
                '"{}" {}'.format(dtype[0], dtype[1].upper())
                for dtype in self.edges_hdf.dtypes()
                if dtype[0] in valid_edge
            ]
        )

        for dtype in self.edges_hdf.dtypes():
            if dtype[0] in valid_edge:
                if dtype[1].upper() == "NVARCHAR":
                    _cols.append('"{}" {}(5000)'.format(dtype[0], dtype[1].upper()))
                else:
                    _cols.append('"{}" {}'.format(dtype[0], dtype[1].upper()))

        return ", ".join(_cols)

    def drop(self, include_vertices=False, include_edges=False):
        """
        Drops the current graph workspace and all the associated procedures.

        You can also specify to delete the vertices and edges tables if
        required.

        **Note:** The instance of the graph object is not usable anymore
        afterwards.

        Parameters
        ----------
        include_vertices : bool, optional, default: False
            Also drop the Vertices Table

        include_edges : bool, optional, default: False
            Also drop the Edge Table
        """
        try:
            self.connection_context.connection.cursor().execute(
                """DROP GRAPH WORKSPACE "{}"."{}" """.format(
                    self.schema, self.workspace_name
                )
            )
        except dbapi.Error as error:
            if "invalid graph workspace name:" in error.errortext:
                pass
            else:
                logger.error(error.errortext)

        if include_edges:
            try:
                self.connection_context.connection.cursor().execute(
                    "DROP TABLE {}".format(self.edge_tbl_name)
                )
            except dbapi.Error as error:
                if "invalid table" in error.errortext:
                    pass
                else:
                    logger.error(error.errortext)

        if include_vertices:
            try:
                self.connection_context.connection.cursor().execute(
                    "DROP TABLE {}".format(self.vertex_tbl_name)
                )
            except dbapi.Error as error:
                if "invalid table" in error.errortext:
                    pass
                else:
                    logger.error(error.errortext)

    def _create_graph(self):
        """
        Explicitly create the graph workspace.

        Returns
        -------

        """
        sql = 'DROP GRAPH WORKSPACE "{}"."{}"'.format(self.schema, self.workspace_name)

        try:
            self.connection_context.connection.cursor().execute(sql)
        except dbapi.Error as error:
            if "invalid graph workspace name:" in error.errortext:
                pass
            else:
                logger.error(error.errortext)

        sql = """
            CREATE GRAPH WORKSPACE "{schema}"."{workspace_name}"
            EDGE TABLE "{schema}"."{edge_table}" 
            SOURCE COLUMN "{source_column}" 
            TARGET COLUMN "{target_column}" 
            KEY COLUMN "{edge_id}"
            VERTEX TABLE "{schema}"."{vertex_table}" 
            KEY COLUMN "{vertex_key_column}"
        """.format(
            workspace_name=self.workspace_name,
            schema=self.schema,
            edge_table=self.edge_tbl_name,
            edge_id=self.edge_key_column,
            vertex_table=self.vertex_tbl_name,
            source_column=self.edge_source_column,
            target_column=self.edge_target_column,
            vertex_key_column=self.vertex_key_column,
        )

        try:
            self.connection_context.connection.cursor().execute(sql)
        except dbapi.Error as error:
            logger.error(error.errortext)

    @staticmethod
    def _spatial_transform(hdf, pdf):
        """
        If the hana dataframe has geo_cols, transform the cols into pandas
        ready format. Used internally when a pandas dataframe is returned
        without using collect().

        Parameters
        ----------
        hdf : HANA Dataframe
            Checked for geo_cols.
        pdf : Pandas Dataframe
            Transformed if containing spatial data.

        Returns
        -------
        pd.Dataframe

        """
        if hdf.geo_cols:
            for geo in list(hdf.geo_cols.keys()):
                # Use the HANA Dataframe method typically used by hdf.collect()
                # if there are geo cols.
                pdf = hdf._transform_geo_column(  # pylint: disable=protected-access
                    pandas_df=pdf, col=geo
                )

        return pdf

    def _check_vertex_exists_by_key(self, vertices):
        """
        Change a list of vertex keys into a string and filter on them to
        check if they are in the graph. Raise a ValueError if any of the
        keys are not recognized in the vertex table. Edge case is possible
        where source tables are not up to date of the workspace.

        Parameters
        ----------
        vertices : list
            Vertex keys expected to be in the graph.

        Returns
        -------
        bool : True if the vertices exist otherwise ValueError raised.

        """
        vertex_str = ", ".join(["'{}'".format(vertex) for vertex in vertices])
        cur = self.connection_context.connection.cursor()

        cur.execute(
            """
        SELECT "{key}" FROM "{sch}"."{tbl}" where "{tbl}"."{key}" IN ({vertex_str})
        """.format(
                key=self.vertex_key_column,
                sch=self.schema,
                tbl=self.vertex_tbl_name,
                vertex_str=vertex_str,
            )
        )

        vertex_check = cur.fetchall()

        if len(vertex_check) < len(vertices):
            missing = ", ".join(
                list(
                    filter(
                        lambda vertex_key: vertex_key
                        not in [key[0] for key in vertex_check],
                        [str(key) for key in vertices],
                    )
                )
            )

            logger.error(
                "%s not recognized key(s) in %s", missing, self.vertex_tbl_name
            )
            raise ValueError(
                "{} not recognized key(s) in {}".format(missing, self.vertex_tbl_name)
            )

        return True

    def vertices(self, vertex_key=None):
        """
        Get the table representing vertices within a graph. If there is
        a vertex, check it.

        Parameters
        ----------
        vertex_key : str, optional
            Vertex keys expected to be in the graph.

        Returns
        -------
        pd.Dataframe

        """
        if not vertex_key:
            pdf = self.vertices_hdf.collect()
        elif self._check_vertex_exists_by_key([vertex_key]):
            cur = self.connection_context.connection.cursor()
            cur.execute(
                """SELECT * FROM "{sch}"."{vertex_tbl}" WHERE "{v_key_col}" = '{v_key}' """.format(
                    sch=self.schema,
                    vertex_tbl=self.vertex_tbl_name,
                    v_key_col=self.vertex_key_column,
                    v_key=vertex_key,
                )
            )
            pdf = pd.DataFrame(cur.fetchall(), columns=self.vertices_hdf.columns)
            pdf = self._spatial_transform(hdf=self.vertices_hdf, pdf=pdf)
        else:
            raise ValueError(
                "Vertex key not recognized in the graph {}.".format(self.workspace_name)
            )

        return pdf

    def edges(self, vertex_key=None, edge_key=None, direction=DEFAULT_DIRECTION):
        """
        Get the table representing edges within a graph. If there is a
        vertex_key, then only get the edges respective to that vertex.

        Parameters
        ----------
        vertex_key : str, optional
            Vertex key from which to get edges.

            Defaults to None.

        edge_key : str, optional
            Edge key from which to get edges.

            Defaults to None.

        direction : str, optional
            OUTGOING, INCOMING, or ANY which determines the algorithm
            results. Only applicable if vertex_key is not None.

            Defaults to OUTGOING.

        Returns
        -------
        pd.Dataframe

        """
        pdf = None

        if vertex_key:
            if self._check_vertex_exists_by_key([vertex_key]):
                if direction == DIRECTION_ANY:
                    cur = self.connection_context.connection.cursor()
                    cur.execute(
                        """
                            SELECT * FROM "{sch}"."{wks}"
                            WHERE "{src}" = '{v_key}' OR "{tgt}" = '{v_key}'
                        """.format(
                            sch=self.schema,
                            wks=self.edge_tbl_name,
                            src=self.edge_source_column,
                            tgt=self.edge_target_column,
                            v_key=vertex_key,
                        )
                    )
                    pdf = pd.DataFrame(cur.fetchall(), columns=self.edges_hdf.columns)
                elif direction == DIRECTION_INCOMING:
                    pdf = self.in_edges(vertex_key=vertex_key)
                elif direction == DIRECTION_OUTGOING:
                    pdf = self.out_edges(vertex_key=vertex_key)
            else:
                raise ValueError(
                    "Vertex key not recognized in the graph {}.".format(
                        self.workspace_name
                    )
                )

            # Take care of the geo_cols that aren't processed unless with the hdf
            # collect method
            pdf = self._spatial_transform(hdf=self.edges_hdf, pdf=pdf)
        elif edge_key:
            cur = self.connection_context.connection.cursor()

            cur.execute(
                """SELECT * FROM "{sch}"."{wks}" WHERE "{key_col}" = '{e_key}' """.format(
                    sch=self.schema,
                    wks=self.edge_tbl_name,
                    key_col=self.edge_key_column,
                    e_key=edge_key,
                )
            )

            result = pd.DataFrame(cur.fetchall(), columns=self.edges_hdf.columns)

            if result.size == 0:
                raise KeyError(
                    "No edge with {} {}".format(self.edge_key_column, edge_key)
                )
            else:
                pdf = result
                # Take care of the geo_cols that aren't processed unless with the
                # hdf collect method
                pdf = self._spatial_transform(hdf=self.edges_hdf, pdf=pdf)
        elif not vertex_key and not edge_key:
            pdf = self.edges_hdf.collect()

        return pdf

    def out_edges(self, vertex_key):
        """
        Get the table representing edges within a graph filtered on a
        vertex_key and its outgoing edges.

        Parameters
        ----------
        vertex_key : str
            Vertex key from which to get edges.

        Returns
        -------
        pd.Dataframe

        """
        if self._check_vertex_exists_by_key([vertex_key]):
            cur = self.connection_context.connection.cursor()

            cur.execute(
                """
                    SELECT * FROM "{sch}"."{wks}" WHERE "{src}" = '{v_key}'
                """.format(
                    sch=self.schema,
                    wks=self.edge_tbl_name,
                    src=self.edge_source_column,
                    v_key=vertex_key,
                )
            )

            return pd.DataFrame(cur.fetchall(), columns=self.edges_hdf.columns)
        else:
            raise ValueError(
                "Vertex key not recognized in the graph {}.".format(self.workspace_name)
            )

    def source(self, edge_key):
        """
        Get the vertex that is the source/from/origin/start point of an
        edge.

        Parameters
        ----------
        edge_key : str
            Edge key from which to get source vertex.

        Returns
        -------
        pd.Dataframe

        """
        cur = self.connection_context.connection.cursor()

        cur.execute(
            """
                SELECT "{src}" FROM "{sch}"."{edge_tbl}" WHERE "{e_key_col}" = '{e_key}'
            """.format(
                src=self.edge_source_column,
                sch=self.schema,
                edge_tbl=self.edge_tbl_name,
                e_key_col=self.edge_key_column,
                e_key=edge_key,
            )
        )
        return self.vertices(vertex_key=cur.fetchone()[0])

    def target(self, edge_key):
        """
        Get the vertex that is the source/from/origin/start point of an
        edge.

        Parameters
        ----------
        edge_key : str
            Edge key from which to get source vertex.

        Returns
        -------
        pd.Dataframe

        """
        cur = self.connection_context.connection.cursor()

        cur.execute(
            """
                SELECT "{tgt}" FROM "{sch}"."{edge_tbl}" WHERE "{e_key_col}" = '{e_key}'
            """.format(
                tgt=self.edge_target_column,
                sch=self.schema,
                edge_tbl=self.edge_tbl_name,
                e_key_col=self.edge_key_column,
                e_key=edge_key,
            )
        )

        return self.vertices(vertex_key=cur.fetchone()[0])

    def in_edges(self, vertex_key):
        """
        Get the table representing edges within a graph filtered on a
        vertex_key and its incoming edges.

        Parameters
        ----------
        vertex_key : str
            Vertex key from which to get edges.

        Returns
        -------
        pd.Dataframe

        """
        if self._check_vertex_exists_by_key([vertex_key]):
            cur = self.connection_context.connection.cursor()

            cur.execute(
                """
                    SELECT * FROM "{sch}"."{wks}" WHERE "{tgt}" = '{v_key}'
                """.format(
                    sch=self.schema,
                    wks=self.edge_tbl_name,
                    tgt=self.edge_target_column,
                    v_key=vertex_key,
                )
            )
            return pd.DataFrame(cur.fetchall(), columns=self.edges_hdf.columns)
        else:
            raise ValueError(
                "Vertex key not recognized in the graph {}.".format(self.workspace_name)
            )

    def _neighbors_generic(
        self, direction, lower_bound, start_vertex, upper_bound, include_edges=False
    ):
        """
        Generic Method to read the neighbors with or without the edges

        :param direction:
        :param lower_bound:
        :param start_vertex:
        :param upper_bound:
        :param include_edges:
        :return: Cursor from the SQL query result
        """
        if upper_bound and lower_bound:
            if upper_bound < lower_bound:
                raise ValueError(
                    "Max depth (upper_bound) {} is less than min depth (lower_bound) {}".format(
                        upper_bound, lower_bound
                    )
                )

        # Check Direction
        direction = direction.upper()
        if direction not in DIRECTIONS:
            raise KeyError(
                "Direction needs to be one of {}".format(", ".join(DIRECTIONS))
            )

        # run validation/existence checks
        self._check_vertex_exists_by_key([start_vertex])
        # Get the column data types for each table and create the vertices / edges
        # graph_script tables if dtypes are valid for graph

        vertex_columns = self._vertex_columns()
        vertex_select = ", ".join(
            [
                ':v."{}"'.format(col)
                for col in self.vertices_hdf.columns
                if col == self.vertex_key_column
            ]
        )

        valid_edge = None
        interface_sql = ""
        edges_sql = ""
        if include_edges:
            valid_edge = [
                self.edge_key_column,
                self.edge_target_column,
                self.edge_source_column,
            ]  # filter only required cols
            edge_columns = self._edge_columns(valid_edge=valid_edge)

            interface_sql = ",OUT o_edges TABLE ({edge_columns}) => ?".format(
                edge_columns=edge_columns
            )

            edge_select = ", ".join(
                [
                    ':e."{}"'.format(dtype[0])
                    for dtype in self.edges_hdf.dtypes()
                    if dtype[0] in valid_edge
                ]
            )

            edges_sql = """
                            MULTISET<Edge> m_edges = Edges(:g, :m_neighbors, :m_neighbors);
                            o_edges = SELECT {edge_select} FOREACH e IN :m_edges; 
            """.format(
                edge_select=edge_select
            )

        cur = self.connection_context.connection.cursor()
        sql = """
                DO (
                    IN i_startVertex {vertex_key_col_dtype} => '{start_vertex}', 
                    IN min_depth BIGINT => {min_depth}, 
                    IN max_depth BIGINT => {max_depth}, 
                    IN i_dir VARCHAR(10) => '{direction}', 
                    OUT o_vertices TABLE ({vertex_columns}) => ?
                    {interface_sql}
                )
                LANGUAGE GRAPH
                BEGIN 
                    GRAPH g = Graph("{schema}", "{workspace}"); 
                    VERTEX v_start = Vertex(:g, :i_startVertex); 
 
                    MULTISET<Vertex> m_neighbors = Neighbors(:g, :v_start, 
                        :min_depth, :max_depth, :i_dir);
                    o_vertices = SELECT {vertex_select} FOREACH v IN :m_neighbors;
                    
                    {edges_sql}
                END;
              """.format(
            vertex_key_col_dtype=self.vertex_key_col_dtype,
            start_vertex=start_vertex,
            min_depth=lower_bound,
            max_depth=upper_bound,
            direction=direction,
            vertex_columns=vertex_columns,
            interface_sql=interface_sql,
            schema=self.schema,
            workspace=self.workspace_name.upper(),
            vertex_select=vertex_select,
            edges_sql=edges_sql,
        )

        try:
            cur.executemany(sql)
        except dbapi.Error as err:
            raise RuntimeError(err.errortext)
        return cur, valid_edge

    def neighbors_with_edges(
        self,
        start_vertex,
        direction: str = DEFAULT_DIRECTION,
        lower_bound=1,
        upper_bound=1,
    ) -> Path:
        """
        Get a virtual subset of the graph based on a start_vertex and all
        vertices within a lower_bound->upper_bound count of degrees of
        separation. The result is similar to :func:`~hana_ml.graph.Graph.neighbors`
        but includes edges which could be useful for visualization.

        **Note:** The edges table also contains edges between neighbors,
        if there are any (not only edges from the start vertex).

        Parameters
        ----------
        start_vertex : str
            Source from which the subset is based.
        direction : str, optional
            OUTGOING, INCOMING, or ANY which determines the algorithm results.

            Defaults to None.
        lower_bound : int, optional
            The count of degrees of separation from which to start considering
            neighbors.
            If you want to include the start node into consideration,
            set `lower_bound=0`. In this case you will also get edges
            from the start node to the neighbors (Ego Graph)

            Defaults to 1.
        upper_bound : int, optional
            The count of degrees of separation at which to end considering neighbors.

            Defaults to 1.

        Returns
        -------
        Path
            Class representing the Pandas Dataframes that resulted from the function.

        """
        cur, valid_edge = self._neighbors_generic(
            direction, lower_bound, start_vertex, upper_bound, include_edges=True
        )

        # Build the response from the result sets
        vertices = pd.DataFrame(
            cur.fetchall(),
            columns=[
                col
                for col in self.vertices_hdf.columns
                if col == self.vertex_key_column
            ],
        )

        cur.nextset()
        edges = pd.DataFrame(
            cur.fetchall(),
            columns=[col for col in self.edges_hdf.columns if col in valid_edge],
        )

        return Path(vertices=vertices, edges=edges)

    def neighbors(
        self,
        start_vertex,
        direction: str = DEFAULT_DIRECTION,
        lower_bound=1,
        upper_bound=1,
    ) -> pd.DataFrame:
        """
        Get a virtual subset of the graph based on a start_vertex and all
        vertices within a lower_bound->upper_bound count of degrees of
        separation. The result is similar to :func:`~hana_ml.graph.Graph.neighbors_with_edges`
        but only includes nodes/vertices not the edges.

        Parameters
        ----------
        start_vertex : str
            Source from which the subset is based.
        direction : str, optional
            OUTGOING, INCOMING, or ANY which determines the algorithm
            results.

            Defaults to None.
        lower_bound : int, optional
            The count of degrees of separation from which to start
            considering neighbors. If you want to include the start node
            into consideration, set `lower_bound=0`.

            Defaults to 1.
        upper_bound : int, optional
            The count of degrees of separation at which to end
            considering neighbors.

            Defaults to 1.

        Returns
        -------
        pd.Dataframe
            A Pandas Dataframe that contains the nodes/vertices
            representing the result of the algorithm.

        """
        cur, valid_edge = self._neighbors_generic(  # pylint: disable=unused-variable
            direction, lower_bound, start_vertex, upper_bound, include_edges=False
        )

        results = cur.fetchall()

        return pd.DataFrame(
            results,
            columns=[
                col
                for col in self.vertices_hdf.columns
                if col == self.vertex_key_column
            ],
        )

    def shortest_path(
        self, source, target, weight=None, direction=DEFAULT_DIRECTION
    ) -> Path:
        """
        Given a source and target vertex_key with optional weight and
        direction, get the shortest path between them.
        The procedure may fail for HANA versions prior to SP05 therefore
        a switch to determine the version is provided.
        The user can take the results and visualize them with libraries
        such as networkX using the `result.edges()`.

        Parameters
        ----------
        source : str
            vertex key from which the shortest path will start.
        target : str
            vertex key from which the shortest path will end.
        weight : str, optional
            Variable for column name to which to apply the weight.

            Defaults to None.
        direction : str, optional
            OUTGOING, INCOMING, or ANY which determines the algorithm results.

            Defaults to OUTGOING.

        Returns
        -------
        Path : Path
            Class representing the Pandas Dataframes that resulted from
            the function.

        Examples
        --------
        >>> path1 = hana_graph.shortest_path(source='3', target='5', weight='rating')
        >>> nx_graph1 = nx.from_pandas_edgelist(path1.edges(),
        >>> ... source=edge_source_column, target=edge_target_column)
        >>> fig3, ax3 = plt.subplots(1, 1, figsize=(80, 80))
        >>> nx.draw_networkx(nx_graph1, ax=ax3)

        """
        # Version check
        if int(self.connection_context.hana_major_version()) < 4:
            raise EnvironmentError(
                "SAP HANA version is not compatible with this method"
            )

        # Check Direction
        direction = direction.upper()
        if direction not in DIRECTIONS:
            raise KeyError(
                "Direction needs to be one of {}".format(", ".join(DIRECTIONS))
            )

        # Set procedure name and run validation/existence checks
        self._check_vertex_exists_by_key([source, target])

        # Get the column data types for each table and create the vertices/edges
        # graph_script tables if dtypes are valid for graph
        valid_edge = [
            self.edge_key_column,
            self.edge_target_column,
            self.edge_source_column,
        ]  # filter only required cols

        # Convert the columns to strings for the SQL statement
        vertex_columns = self._vertex_columns()
        edge_columns = self._edge_columns(valid_edge=valid_edge)

        vertex_select = ", ".join(
            [
                ':v."{}"'.format(dtype[0])
                for dtype in self.vertices_hdf.dtypes()
                if dtype[0] == self.vertex_key_column
            ]
        )

        edge_select = ", ".join(
            [
                ':e."{}"'.format(dtype[0])
                for dtype in self.edges_hdf.dtypes()
                if dtype[0] in valid_edge
            ]
        )

        # SQL to create and run procedure
        if weight:
            weighted_definition = """
                                    WeightedPath<DOUBLE> p = Shortest_Path(:g, :v_start,
                                    :v_end, (Edge e) => DOUBLE{{ return :e."{weight}"; }},
                                    :i_direction);
                                  """.format(
                weight=weight
            )
        else:
            weighted_definition = """
                                    WeightedPath<BIGINT> p = Shortest_Path(:g, :v_start,
                                    :v_end, :i_direction);
                                  """

        sql = """
                DO (
                    IN i_startVertex {vertex_dtype} => '{start_vertex}',
                    IN i_endVertex {vertex_dtype} => '{end_vertex}',
                    IN i_direction NVARCHAR(10) => '{direction}',
                    OUT o_vertices TABLE ({vertex_columns}, "VERTEX_ORDER" BIGINT) => ?,
                    OUT o_edges TABLE ({edge_columns}, "EDGE_ORDER" BIGINT) => ?,
                    OUT o_scalars TABLE ("WEIGHT" DOUBLE) => ?
                )
                LANGUAGE GRAPH
                BEGIN
                    GRAPH g = Graph("{schema}", "{workspace}");
                    VERTEX v_start = Vertex(:g, :i_startVertex);
                    VERTEX v_end = Vertex(:g, :i_endVertex);
                    
                    {weighted_definition}
                    
                    o_vertices = SELECT {vertex_select}, :VERTEX_ORDER FOREACH v 
                                 IN Vertices(:p) WITH ORDINALITY AS VERTEX_ORDER;
                    o_edges = SELECT {edge_select}, :EDGE_ORDER FOREACH e 
                              IN Edges(:p) WITH ORDINALITY AS EDGE_ORDER;
                              
                    DOUBLE p_weight= DOUBLE(WEIGHT(:p));
                    o_scalars."WEIGHT"[1L] = :p_weight;
                END;
              """.format(
            schema=self.schema,
            vertex_dtype=self.vertex_key_col_dtype,
            start_vertex=source,
            end_vertex=target,
            direction=direction,
            vertex_columns=vertex_columns,
            edge_columns=edge_columns,
            workspace=self.workspace_name.upper(),
            weighted_definition=weighted_definition,
            vertex_select=vertex_select,
            edge_select=edge_select,
        )

        try:
            cur = self.connection_context.connection.cursor()
            cur.executemany(sql)
        except dbapi.Error as err:
            raise RuntimeError(err.errortext)

        # Build the response from the result sets
        # Vertices
        vertex_cols = [
            col for col in self.vertices_hdf.columns if col == self.vertex_key_column
        ]
        vertex_cols.append("VERTEX_ORDER")
        vertices = pd.DataFrame(cur.fetchall(), columns=vertex_cols)

        # Edges
        cur.nextset()
        edge_rows = cur.fetchall()
        edge_cols = [col for col in self.edges_hdf.columns if col in valid_edge]
        edge_cols.append("EDGE_ORDER")
        edges = pd.DataFrame(edge_rows, columns=edge_cols)

        # Weight from the scalar table
        weight = None
        cur.nextset()
        scalars = cur.fetchall()
        if len(scalars) > 0:
            weight = scalars[0].column_values[0]

        return Path(vertices=vertices, edges=edges, weight=weight)

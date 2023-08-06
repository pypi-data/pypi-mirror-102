from lumipy.common.ipython_utils import live_status_in_cell
from lumipy.query.expression.base_sql_expression import BaseSqlExpression
from lumipy.query.expression.column.column_literal import LiteralColumn
from lumipy.query.expression.sql_value_type import SqlValType
from lumipy.query.expression.table_op.base_table_op import BaseTableExpression
from IPython.core.display import clear_output
from pandas import DataFrame


class CreateView(BaseSqlExpression):
    """Class that represents addition of pragma lines at the top of your query that create a view.

    """

    def __init__(self, view_path: str, commit: str, query: BaseTableExpression):
        """__init__ method of the CreateView class

        Args:
            view_path (str): string that defines the view path. Must be just alphanumerics and '/'. For example
            A/B/C/MyView will become a view called A.B.C.MyView.
            commit (str): commit message describing the creation/update of the view.
            query (BaseTableExpression): query that the view is built from.
        """
        if any(not c.isalnum() and c != '/' for c in view_path) or len(view_path) == 0:
            raise ValueError(
                "Input value for view_path must be non-empty string made up of alphanumeric characters + '/'. "
                f"Was '{view_path}'"
            )
        if len(commit) == 0 or not isinstance(commit, str):
            raise ValueError(f"Commit message value must be a non-empty string. Was '{commit}'.")
        if not issubclass(type(query), BaseTableExpression):
            raise ValueError(
                f"Query input must be a table expression (e.g. select, where, limit). Was {type(query).__name__}."
            )

        view_path_lit = LiteralColumn(view_path)
        commit_lit = LiteralColumn(commit)

        self._client = query.get_client()

        def create_view_sql(vp, c, q):
            return '\n'.join([
                f"pragma ViewPath = {vp.get_sql()};",
                f"pragma CommitMessage = {c.get_sql()};\n",
                q.get_sql()
                ])

        super().__init__(
            "create view",
            create_view_sql,
            lambda *x: True,
            lambda *x: SqlValType.Unit,
            view_path_lit,
            commit_lit,
            query
        )

    def go(self) -> DataFrame:
        """Send query off to Luminesce, monitor progress and then get the result back as a pandas dataframe.

        Returns:
            DataFrame: the result of the query as a pandas dataframe.
        """
        ex_id = 'N/A'
        try:
            ex_id = self._client.start_query(self.get_sql())
            live_status_in_cell(self._client, ex_id)
            df = self._client.get_result(ex_id)
            clear_output(wait=True)
            return df
        except KeyboardInterrupt as ki:
            print("Cancelling query... 💥")
            self._client.delete_query(ex_id)
            raise ki
        except Exception as e:
            raise e

    def print_sql(self):
        """Print the SQL that this expression resolves to.

        """
        print(self.get_sql())

    def go_async(self) -> str:
        """Just send the query to luminesce. Don't monitor progress or fetch result.

        Returns:
            str: the execution ID of the query.
        """
        ex_id = self._client.start_query(self.get_sql())
        print(f"Query running as {ex_id}")
        return ex_id

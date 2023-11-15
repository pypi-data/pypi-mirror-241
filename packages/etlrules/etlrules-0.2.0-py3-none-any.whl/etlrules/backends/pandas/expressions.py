from pandas import Series

from etlrules.backends.common.expressions import Expression as ExpressionBase


class Expression(ExpressionBase):

    def eval(self, df):
        try:
            expr_series = eval(self._compiled_expr, {}, {'df': df})
        except TypeError:
            # attempt to run a slower apply
            expr = self._compiled_expr
            if df.empty:
                expr_series = Series([], dtype="string")
            else:
                expr_series = df.apply(lambda df: eval(expr, {}, {'df': df}), axis=1)
        return expr_series

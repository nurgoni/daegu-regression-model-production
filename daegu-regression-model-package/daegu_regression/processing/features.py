from typing import List

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class YearBinning(BaseEstimator, TransformerMixin):

    def __init__(self, variables: List[str]):

        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables
        self.lower_limit = [1978, 1982, 1988, 1992, 1998, 2002, 2007, 2013, 2018]
        self.year_bin = [
                        "1978-1982",
                        "1982-1988",
                        "1988-1992",
                        "1992-1998",
                        "1998-2002",
                        "2002-2007",
                        "2007-2013",
                        "2013-2018"
                    ]

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()

        for var in self.variables:
            X[var] = pd.cut(
                X[var],
                bins=self.lower_limit,
                labels=self.year_bin,
                include_lowest=True
            )

        return X

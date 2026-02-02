import pandas as pd

def check_missing(df: pd.DataFrame) -> dict:
    return df.isnull().sum().to_dict()

def check_duplicates(df: pd.DataFrame) -> int:
    return int(df.duplicated().sum())

def check_schema(df: pd.DataFrame) -> dict:
    return {"status": "merged schema logic"}


def check_outliers(df: pd.DataFrame) -> dict:
    outliers = {}
    numeric_cols = df.select_dtypes(include="number")

    for col in numeric_cols:
        q1 = numeric_cols[col].quantile(0.25)
        q3 = numeric_cols[col].quantile(0.75)
        iqr = q3 - q1
        outliers[col] = int(
            ((numeric_cols[col] < q1 - 1.5 * iqr) |
             (numeric_cols[col] > q3 + 1.5 * iqr)).sum()
        )

    return outliers

def outlier_count(df):
    """
    Count outliers per numeric column using IQR.
    """
    outliers = {}

    for col in df.select_dtypes(include="number").columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        count = ((df[col] < lower) | (df[col] > upper)).sum()
        outliers[col] = int(count)

    return outliers


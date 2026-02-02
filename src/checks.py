import pandas as pd

def check_missing(df: pd.DataFrame) -> dict:
    """Return count of missing values per column"""
    return df.isnull().sum().to_dict()

def check_missing_percentage(df: pd.DataFrame) -> dict:
    """Return missing percentage per column"""
    return (df.isnull().mean() * 100).round(2).to_dict()

def check_duplicates(df: pd.DataFrame) -> int:
    """Return number of duplicate rows"""
    return int(df.duplicated().sum())

def check_schema(df: pd.DataFrame, expected_columns=None) -> dict:
    """Return missing columns compared to expected schema"""
    if expected_columns is None:
        expected_columns = []
    missing_cols = list(set(expected_columns) - set(df.columns))
    return {"missing_columns": missing_cols}

def check_outliers(df: pd.DataFrame) -> dict:
    """Detect numeric column outliers using IQR method"""
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

def outlier_count(df: pd.DataFrame) -> dict:
    """Count outliers per numeric column using IQR"""
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

import pandas as pd


def transform(df: pd.DataFrame):
    df = df.dropna(how="all")
    df = df.drop_duplicates()

    return df

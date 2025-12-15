import pandas as pd


def extract():
    """
    Docstring for extract
    """
    data_demo = [
        {"id": 1, "name": "Alice", "date": "2024/01/01"},
        {"id": 2, "name": "Bob", "date": "2024/01/01"},
        {"id": 2, "name": "Bob", "date": "2024/01/02"},
        {"id": 3, "name": None, "date": "2024/01/03"},
        {"id": None, "name": None, "date": None},
    ]

    df = pd.DataFrame(data_demo)
    return df

from extract import extract
from transform import transform
from load import load


def main():
    try:
        print("job started")
        df = extract()
        df = transform(df)
        load(df)
        print("job end")
    except Exception as e:
        print(f"{e}")

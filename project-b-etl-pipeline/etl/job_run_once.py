from extract import extract
from transform import transform
from load import load
from etl_runs import track_etl_run


def main():
    with track_etl_run("demo_etl_job"):
        print("job started")
        df = extract()
        df = transform(df)
        load(df)
        print("job end")

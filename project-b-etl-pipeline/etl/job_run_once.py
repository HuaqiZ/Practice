import time
from etl.extract import extract
from etl.transform import transform
from etl.load import load
from etl.etl_runs import track_etl_run

MAX_RETRIES = 3


def main():
    for i in range(1, MAX_RETRIES + 1):
        try:
            with track_etl_run("demo_etl_job"):
                print(f"job started {i} times")
                df = extract()
                df = transform(df)
                load(df)
                print("job end")
            return
        except Exception as e:
            print(f"{i} times failed, {e}")

            if i == MAX_RETRIES:
                raise

            time.sleep(2**i)


if __name__ == "__main__":
    main()

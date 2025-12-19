import psycopg2
import os
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()


@contextmanager
def track_etl_run(job_name: str):
    conn = psycopg2.connect(os.getenv("DB_URL"))
    cur = conn.cursor()
    cur.execute(
        """
            INSERT INTO etl_runs(job_name, status)
            VALUES(%s, 'running')
            RETURNING id
        """,
        (job_name,),
    )
    run_id = cur.fetchone()[0]
    conn.commit()
    try:
        yield
        cur.execute(
            """
                UPDATE etl_runs
                SET status = 'success', end_time = NOW()
                        WHERE id = %s
            """,
            (run_id,),
        )
        conn.commit()
    except Exception as e:
        cur.execute(
            """
                UPDATE etl_runs
                SET status = 'failed', end_time = NOW(), message=%s
                WHERE id = %s    
            """,
            (str(e), run_id),
        )
        conn.commit()
        raise
    finally:
        cur.close()
        conn.close()

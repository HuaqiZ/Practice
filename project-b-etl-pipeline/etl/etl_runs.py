from contextlib import contextmanager
from dotenv import load_dotenv
import traceback
from common.db import connect

load_dotenv()


@contextmanager
def track_etl_run(job_name: str):
    conn = connect()
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
        full_msg = traceback.format_exc()
        cur.execute(
            """
                UPDATE etl_runs
                SET status = 'failed', end_time = NOW(), message=%s
                WHERE id = %s    
            """,
            (full_msg, run_id),
        )
        conn.commit()
        raise
    finally:
        cur.close()
        conn.close()

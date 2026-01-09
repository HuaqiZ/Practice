from common.db import fetch


def get_latest_run():
    rows = fetch(
        "SELECT id, job_name, start_time, end_time, status, message FROM etl_runs ORDER BY start_time DESC LIMIT 1"
    )
    if not rows:
        return None
    row = rows[0]
    return {
        "id": row[0],
        "job_name": row[1],
        "start_time": row[2],
        "end_time": row[3],
        "status": row[4],
        "message": row[5],
    }


def get_recent_runs(limit: int = 20):
    rows = fetch(
        "SELECT id, job_name, start_time, end_time, status, message FROM etl_runs ORDER BY start_time DESC LIMIT %s",
        (limit,),
    )
    return [
        {
            "id": row[0],
            "job_name": row[1],
            "start_time": row[2],
            "end_time": row[3],
            "status": row[4],
            "message": row[5],
        }
        for row in rows
    ]

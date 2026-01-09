from typing import List
from fastapi import FastAPI, HTTPException, Query
from .models import RunRecord
from .queries import get_latest_run, get_recent_runs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/runs/latest", response_model=RunRecord)
def latest_run():
    run = get_latest_run()
    if not run:
        raise HTTPException(status_code=404, detail="No runs found")
    return run


@app.get("/runs", response_model=List[RunRecord])
def recent_runs(limit: int = Query(20, ge=1, le=100)):
    return get_recent_runs(limit)

# Project B – ETL Pipeline with Monitoring

This project implements a simple local ETL pipeline that ingests batch CSV data, transforms it using pandas, stores the results in Postgres, and exposes pipeline metrics through a FastAPI service running on localhost.

The project is designed for learning and interview demonstration purposes and is not Dockerized.

## Architecture

CSV Files → ETL (pandas) → Postgres → FastAPI (metrics API) → Next.js Monitoring UI

## Tech Stack

- Python
- pandas
- Postgres
- FastAPI

## How to Run

> This project runs locally only (no Docker).  
> All services are exposed on `localhost`.

### 1.Setup Environment

```bash
pip install -r requirements.txt
```

### 2.Setup Postgres

Create database:
CREATE DATABASE etl_runs;
Configure connection (e.g. `.env`):

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=etl_runs
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
```

### 3.Run ETL Job

python etl/job_run_once.py

### 4. Start Monitoring API

uvicorn api.main:app --reload
Access API and docs:
http://localhost:8000
http://localhost:8000/docs

## Why pandas

- Fast and readable batch transformations
- Strong data cleaning and type handling
- Well-suited for small-to-medium datasets

## Why Postgres

- Reliable storage with ACID guarantees
- Efficient querying and indexing
- Safe concurrent access
- Easy tracking of pipeline history and metrics

## Scalability Notes

- Use incremental loads as data grows
- Add indexes or partitioning in Postgres
- Move to distributed processing for very large

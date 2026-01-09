# Project A – Realtime Dashboard

## Tech Stack

- Backend: Python, FastAPI
- Database: PostgreSQL
- Frontend: Next.js, Chart.js
- ETL: Python
- Containerization: Docker, Docker Compose

## Public API used:

CoinGecko Markets API  
https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd

## Features

- Fetch cryptocurrency market data from the public API
- Store processed data in PostgreSQL
- Expose data through a FastAPI backend
- Visualize real-time data in a dashboard

The ETL process is split into two stages:

1. Extract & Transform: fetches data from CoinGecko and stores it as CSV
2. Load: reads CSV data and inserts it into PostgreSQL

> Note: ETL scripts are executed manually for this demo.

## How to Run

Start backend and database:

```bash
docker-compose up --build
```

Start frontend:

```bash
npm run dev
```

> This project is designed to be run locally.
> It is not deployed to avoid keeping Docker containers running continuously.

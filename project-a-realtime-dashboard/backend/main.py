from fastapi import FastAPI
from queries import delete_coin
from routers.prices import router as prices_router

app = FastAPI()

app.include_router(prices_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.delete("/coin/{symbol}")
def delete(symbol: str):
    delete_coin(symbol)
    return {"status": "deleted"}

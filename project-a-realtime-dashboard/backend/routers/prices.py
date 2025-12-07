from fastapi import APIRouter, HTTPException
from models import Price
from queries import get_latest_price

router = APIRouter(prefix="/prices")


@router.get("/latest", response_model=Price)
def price(symbol: str):
    result = get_latest_price(symbol)

    if result is None:
        raise HTTPException(404, f"No data for {symbol}")

    return result

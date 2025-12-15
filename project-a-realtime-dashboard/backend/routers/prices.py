from typing import List
from fastapi import APIRouter, HTTPException
from models import Price
from queries import get_all_price, get_latest_price

router = APIRouter(prefix="/prices")


@router.get("/all", response_model=List[Price])
def priceStatus():
    result = get_all_price()

    if result is None:
        raise HTTPException(404, "No data")

    return result


@router.get("/{symbol}", response_model=Price)
def price(symbol: str):
    result = get_latest_price(symbol)

    if result is None:
        raise HTTPException(404, f"No data for {symbol}")

    return result

from pydantic import BaseModel


class Price(BaseModel):
    id: str
    current_price: float


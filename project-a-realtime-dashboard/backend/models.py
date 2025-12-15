from pydantic import BaseModel


class Price(BaseModel):
    id: str
    name: str
    current_price: float


from pydantic import BaseModel, Field, validator
from typing import Optional

class DataModel(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    price: float
    stock: int
    category: str

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        return value

    @validator("stock")
    def stock_must_be_non_negative(cls, value):
        if value < 0:
            raise ValueError("Stock must be >= 0")
        return value
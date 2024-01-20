from typing import Optional, List
from pydantic import BaseModel

from app.schemas import Color, Size


class ProductBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None

    price: float
    sizes: List[Size]
    colors: List[Color] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(ProductBase):
    # Properties shared by models stored in DB
    id: int
    slug: str

    class Config:
        orm_mode = True


class Product(ProductInDBBase):
    # Properties to return to client
    pass

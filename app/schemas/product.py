from typing import Optional, List
from pydantic import BaseModel, ConfigDict

from .color import Color
from .size import Size


class ProductColorSizeLink(BaseModel):
    product_id: int
    color: Color
    size: Size
    availability: int

    model_config = ConfigDict(from_attributes=True)


class ProductBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(ProductBase):
    # Properties shared by models stored in DB
    id: int
    color_size_combinations: List[ProductColorSizeLink] = []

    model_config = ConfigDict(from_attributes=True)


class Product(ProductInDBBase):
    pass

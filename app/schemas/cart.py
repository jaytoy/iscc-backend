from pydantic import BaseModel


class Cart(BaseModel):
    product_id: int
    product_name: str
    size: str
    color_id: int
    quantity: int

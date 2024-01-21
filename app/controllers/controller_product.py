from typing import Optional

from sqlalchemy.orm import Session, joinedload

from app.controllers.base import ControllerBase
from app.models.product import Product, ProductColorSizeLink
from app.schemas.product import ProductCreate, ProductUpdate


class ControllerProduct(ControllerBase[Product, ProductCreate, ProductUpdate]):
    def get_by_slug(self, db: Session, slug: str) -> Optional[Product]:
        product = db.query(self.model).options(
            joinedload(self.model.color_size_combinations).joinedload(
                ProductColorSizeLink.color),
            joinedload(self.model.color_size_combinations).joinedload(
                ProductColorSizeLink.size)
        ).filter(self.model.slug == slug).first()
        return product


product = ControllerProduct(Product)

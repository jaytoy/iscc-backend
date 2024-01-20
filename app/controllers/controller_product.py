from typing import Optional

from sqlalchemy.orm import Session

from app.controllers.base import ControllerBase
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ControllerProduct(ControllerBase[Product, ProductCreate, ProductUpdate]):
    def get_by_slug(self, db: Session, slug: str) -> Optional[Product]:
        return db.query(self.model).filter(self.model.slug == slug).first()

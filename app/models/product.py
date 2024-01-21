from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class ProductColorSizeLink(Base):
    __tablename__ = 'product_color_size_link'
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    color_id = Column(Integer, ForeignKey('colors.id'), primary_key=True)
    size_id = Column(Integer, ForeignKey('sizes.id'), primary_key=True)
    availability = Column(Integer, default=0)
    product = relationship("Product",
                           back_populates="color_size_combinations")
    color = relationship("Color",
                         back_populates="color_size_combinations")
    size = relationship("Size",
                        back_populates="color_size_combinations")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    image_url = Column(String, index=True)
    color_size_combinations = relationship(
        "ProductColorSizeLink", back_populates="product")

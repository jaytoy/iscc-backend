from sqlalchemy import Column, Integer, String, Float, ForeignKey, ARRAY

from app.database.base_class import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    image = Column(String, index=True)
    size_ids = Column(ARRAY(Integer), ForeignKey('sizes.id'))
    color_ids = Column(ARRAY(Integer), ForeignKey('colors.id'))

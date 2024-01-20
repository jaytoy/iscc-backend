from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Color(Base):
    __tablename__ = "colors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hex_code = Column(String, unique=True)
    color_size_combi = relationship(
        "ProductColorSizeLink", back_populates="color")

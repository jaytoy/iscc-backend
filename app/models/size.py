from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Size(Base):
    __tablename__ = "sizes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    abbreviation = Column(String)
    color_size_combi = relationship(
        "ProductColorSizeLink", back_populates="size")

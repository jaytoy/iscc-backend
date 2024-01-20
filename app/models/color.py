from sqlalchemy import Column, Integer, String

from app.database.base_class import Base


class Color(Base):
    __tablename__ = "colors"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    hex_code = Column(String, unique=True)
    availability = Column(Integer, default=0)

from sqlalchemy import Column, Integer, String

from app.database.base_class import Base


class Size(Base):
    __tablename__ = "sizes"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    abbreviation = Column(String, unique=True)
    availability = Column(Integer, default=0)

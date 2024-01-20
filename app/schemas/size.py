from pydantic import BaseModel


class SizeBase(BaseModel):
    name: str
    abbreviation: str

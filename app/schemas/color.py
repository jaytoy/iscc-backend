from pydantic import BaseModel


class ColorBase(BaseModel):
    name: str
    hex_code: str

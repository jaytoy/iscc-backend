from pydantic import BaseModel, ConfigDict


class ColorBase(BaseModel):
    name: str
    hex_code: str


class ColorInDBBase(ColorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class Color(ColorInDBBase):
    pass

from pydantic import BaseModel, ConfigDict


class SizeBase(BaseModel):
    name: str
    abbreviation: str


class SizeInDBBase(SizeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class Size(SizeInDBBase):
    pass

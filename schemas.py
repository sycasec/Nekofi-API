from pydantic import BaseModel, Field


class Kofi(BaseModel):
    id: int
    title: str
    description: str
    price: float
    isAvailable: bool

class updateKofi(BaseModel):
    title:str = Field(...)
    description:str = Field(...)
    price:float = Field(...)
    isAvailable:bool = Field(...)

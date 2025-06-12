from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date

class VueloBase(SQLModel):
    origen: str = Field(..., min_length=2, max_length=100)
    destine: str = Field(..., min_length=2, max_length=100)
    fecha: date = Field(...)
    capacidad: int = Field(..., ge=1)

class VueloCreate(VueloBase):
    pass

class Vuelo(VueloBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class VueloWithID(SQLModel):
    id: int
    origen: str
    destine: str
    fecha: date
    capacidad: int

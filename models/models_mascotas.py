from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date

class PetsBase(SQLModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    origen: str = Field(..., min_length=2, max_length=100)
    destine: str = Field(..., min_length=2, max_length=100)
    raza: str = Field(..., min_length=2, max_length=100)
    edad: int = Field(..., ge=0)
    fecha: date = Field(...)
    user_id: int = Field(..., foreign_key="user.id")

class PetsCreate(SQLModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    origen: str = Field(..., min_length=2, max_length=100)
    destine: str = Field(..., min_length=2, max_length=100)
    raza: str = Field(..., min_length=2, max_length=100)
    edad: int = Field(..., ge=0)
    fecha: date = Field(...)
    user_id: int = Field(...)

class Pet(PetsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class PetWithID(SQLModel):
    id: int
    nombre: str
    origen: str
    destine: str  # Nombre exacto como en la DB
    edad: int
    raza: str
    fecha: date
    user_id: int

class UpdatedPets(SQLModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    origen: str = Field(..., min_length=2, max_length=100)
    destine: str = Field(..., min_length=2, max_length=100)
    edad: int = Field(..., ge=0)
    fecha: date = Field(...)
    user_id: int = Field(...)
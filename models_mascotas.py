from typing import Optional
from sqlmodel import SQLModel, Field


class PetsBase(SQLModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    origen: str = Field(..., min_length=2, max_length=100)
    destine: str = Field(..., min_length=2, max_length=100)
    raza: str = Field(..., min_length=2, max_length=100)
    edad: int = Field(..., ge=0)
# models_games.py

# models_users.py

class PetsCreate(SQLModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    origen: str = Field(..., min_length=2, max_length=100)
    destine: str = Field(..., min_length=2, max_length=100)
    raza: str = Field(..., min_length=2, max_length=100)
    edad: int = Field(..., ge=0)




class Pet(PetsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class PetWithID(SQLModel):
    id: int
    nombre: str
    origen: str
    destine: str # Nombre exacto como en la DB
    edad: int
    raza: str
class UpdatedPets(SQLModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    origen: str = Field(..., min_length=2, max_length=100)
    destine: str = Field(..., min_length=2, max_length=100)
    edad: int = Field(..., ge=0)
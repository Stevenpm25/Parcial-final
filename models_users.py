from typing import Optional
from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    origen: str = Field(..., min_length=2, max_length=100)
    destine: str = Field(..., min_length=2, max_length=100)
    edad: int = Field(..., ge=0)
# models_games.py

# models_users.py

class UserCreate(SQLModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    origen: str = Field(..., min_length=2, max_length=100)
    destine: str = Field(..., min_length=2, max_length=100)
    edad: int = Field(..., ge=0)




class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class UserWithID(SQLModel):
    id: int
    nombre: str
    origen: str
    destine: str # Nombre exacto como en la DB
    edad: int
class UpdatedUser(SQLModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    origen: str = Field(..., min_length=2, max_length=100)
    destine: str = Field(..., min_length=2, max_length=100)
    edad: int = Field(..., ge=0)
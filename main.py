from fastapi import FastAPI, Depends, Request, HTTPException, Query, UploadFile, File, Form, Body
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from sqlmodel import SQLModel, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from typing import Optional, List, Dict, Any, AsyncGenerator
import os
import csv
import io
import datetime
import random
from dotenv import load_dotenv
from starlette.responses import HTMLResponse
import jinja2
load_dotenv()
from models_users import User, UserWithID, UpdatedUser, UserCreate, User
from models_mascotas import Pet, PetWithID, PetsCreate
app = FastAPI()

from operations_users import (
    read_all_users, read_one_user,
    create_user)
from operations_mascotas import read_all_pets, read_one_pet, create_pet

app = FastAPI(
    title="Parcial Final",
    description="API para usuarios y mascotas",
    version="1.0.0",
    openapi_tags=[{
        "name": "Usuarios",
        "description": "Operaciones con usuarios y mascotas"
    }, {
        "name": "Usuarios",
        "description": "Operaciones con usuarios y mascotas"
    }]
)

# Usa SIEMPRE SQLite local, ignora PostgreSQL
DATABASE_URL = "sqlite+aiosqlite:///petsdb.db"
engine = create_async_engine(
    DATABASE_URL,
    echo=True
)
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)


# Inicializa la base de datos si es SQLite
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


# Dependency
async def get_session() -> AsyncGenerator[Any, Any]:
    async with async_session() as session:
        yield session


@app.get("/api/users", response_model=List[UserWithID], tags=["Users"])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    return await read_all_users(session)

@app.post("/api/users", response_model=UserWithID, tags=["Users"])
async def create_user_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    created_user = await create_user(session, user)
    return created_user


@app.get("/api/pets", response_model=List[PetWithID], tags=["Mascotas"])
async def get_all_pets(session: AsyncSession = Depends(get_session)):
    return await read_all_pets(session)

@app.post("/api/pets", response_model=PetWithID, tags=["Mascotas"])
async def create_pet_pet(pet: PetsCreate, session: AsyncSession = Depends(get_session)):
    created_pet = await create_pet(session, pet)
    return created_pet



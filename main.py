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
app = FastAPI()

from operations_users import (
    read_all_users, read_one_user,
    create_user)

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



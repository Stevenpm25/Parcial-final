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

def get_database_url():
    uri = os.getenv('POSTGRESQL_ADDON_URI')
    if uri:
        return uri.replace("postgresql://", "postgresql+asyncpg://").replace(":5432/", ":50013/")

    return (
        f"postgresql+asyncpg://{os.getenv('POSTGRESQL_ADDON_USER')}:"
        f"{os.getenv('POSTGRESQL_ADDON_PASSWORD')}@"
        f"{os.getenv('POSTGRESQL_ADDON_HOST')}:"
        f"50013/"
        f"{os.getenv('POSTGRESQL_ADDON_DB')}"
    )


try:
    DATABASE_URL = get_database_url()
    print(f"Conectando a la base de datos...")
    print(f"URL: {DATABASE_URL.split('@')[1].split('/')[0]}")  # Muestra solo host:port

    engine = create_async_engine(
        DATABASE_URL,
        echo=True,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=2,
        pool_recycle=300,
        pool_timeout=30
    )
    async_session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

except Exception as e:
    print(f"❌ Error al configurar la base de datos: {str(e)}")
    print("Por favor verifica:")
    print("1. Que tu IP esté autorizada en Clever Cloud")
    print("2. Que las credenciales sean correctas")
    print("3. Que el puerto sea 50013")
    raise


# Dependency
async def get_session() -> AsyncGenerator[Any, Any]:
    async with async_session() as session:
        yield session


@app.get("/api/users", response_model=List[UserWithID], tags=["Users"])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    return await read_all_users(session)

@app.post("/api/users", response_model=UserWithID, tags=["Users"])
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    created_user = await create_user(session, user)
    return created_user



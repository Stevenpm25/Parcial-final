from typing import Sequence, Optional
from sqlmodel import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select as sa_select, func
from models.models_mascotas import *
from models.models_users import User

async def read_all_pets(session: AsyncSession) -> Sequence[Pet]:
    result = await session.execute(select(Pet))
    return result.scalars().all()

async def read_one_pet(session: AsyncSession, pet_id: int) -> Optional[PetWithID]:
    return await session.get(Pet, pet_id)

async def create_pet(session: AsyncSession, pet: PetsCreate) -> Pet:
    new_pet = Pet(**pet.dict())
    session.add(new_pet)
    await session.commit()
    await session.refresh(new_pet)
    return new_pet

async def search_pets(
    session: AsyncSession,
    origen: Optional[str] = None,
    destine: Optional[str] = None,
    fecha: Optional[str] = None,
    user_id: Optional[int] = None
) -> Sequence[Pet]:
    query = select(Pet)
    filters = []
    if origen:
        filters.append(Pet.origen == origen)
    if destine:
        filters.append(Pet.destine == destine)
    if hasattr(Pet, 'fecha') and fecha:
        filters.append(Pet.fecha == fecha)
    if user_id:
        filters.append(Pet.user_id == user_id)
    if filters:
        query = query.where(and_(*filters))
    result = await session.execute(query)
    return result.scalars().all()

async def search_pets_with_user(
    session: AsyncSession,
    origen: Optional[str] = None,
    destine: Optional[str] = None,
    fecha: Optional[str] = None,
    user_id: Optional[int] = None
):
    query = sa_select(Pet, User).join(User, Pet.user_id == User.id)
    filters = []
    if origen:
        filters.append(Pet.origen == origen)
    if destine:
        filters.append(Pet.destine == destine)
    if hasattr(Pet, 'fecha') and fecha:
        filters.append(Pet.fecha == fecha)
    if user_id:
        filters.append(Pet.user_id == user_id)
    if filters:
        query = query.where(and_(*filters))
    result = await session.execute(query)
    return result.all()

async def get_available_flights(
    session: AsyncSession,
    origen: Optional[str] = None,
    destine: Optional[str] = None,
    fecha: Optional[str] = None
):
    query = select(
        Pet.origen,
        Pet.destine,
        Pet.fecha,
        func.count(Pet.id).label("mascotas_registradas")
    )
    filters = []
    if origen:
        filters.append(Pet.origen == origen)
    if destine:
        filters.append(Pet.destine == destine)
    if hasattr(Pet, 'fecha') and fecha:
        filters.append(Pet.fecha == fecha)
    if filters:
        query = query.where(*filters)
    query = query.group_by(Pet.origen, Pet.destine, Pet.fecha)
    result = await session.execute(query)
    return [
        {
            "origen": row.origen,
            "destine": row.destine,
            "fecha": row.fecha,
            "mascotas_registradas": row.mascotas_registradas
        }
        for row in result.fetchall()
    ]

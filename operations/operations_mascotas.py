from typing import Sequence
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.models_mascotas import *

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

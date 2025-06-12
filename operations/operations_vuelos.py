from typing import Sequence, Optional
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.models_vuelos import Vuelo, VueloCreate, VueloWithID

async def read_all_vuelos(session: AsyncSession) -> Sequence[Vuelo]:
    result = await session.execute(select(Vuelo))
    return result.scalars().all()

async def read_one_vuelo(session: AsyncSession, vuelo_id: int) -> Optional[VueloWithID]:
    return await session.get(Vuelo, vuelo_id)

async def create_vuelo(session: AsyncSession, vuelo: VueloCreate) -> Vuelo:
    new_vuelo = Vuelo(**vuelo.dict())
    session.add(new_vuelo)
    await session.commit()
    await session.refresh(new_vuelo)
    return new_vuelo

from typing import Sequence
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.models_users import *

from models.models_users import User


async def read_all_users(session: AsyncSession) -> Sequence[User]:
    result = await session.execute(select(User))
    return result.scalars().all()



async def read_one_user(session: AsyncSession, user_id: int) -> Optional[UserWithID]:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user: UserCreate) -> User:
    new_user = User(**user.dict())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


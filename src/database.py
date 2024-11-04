from typing import AsyncGenerator
from sqlalchemy import   MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import  sessionmaker, declarative_base

from src.config import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_USER
)




DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

Base = declarative_base()
metadata = MetaData()

engine = create_async_engine(DATABASE_URL)
async_session_marker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_marker() as session:
        yield session
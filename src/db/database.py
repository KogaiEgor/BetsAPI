from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import os
from dotenv import load_dotenv
from sqlalchemy.orm import registry

# Загрузка переменных среды из файла .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
ASYNC_DB = os.getenv("DATABASE_URL_ASYNC")
MAIN_DB = os.getenv("MAIN_DB_URL")

# Создание соединения с базой данных
engine = create_async_engine(ASYNC_DB, echo=False)
mapper_registry = registry()
Base = mapper_registry.generate_base()

AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


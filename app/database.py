from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

DATABASE_URL = f"postgresql+asyncpg://postgres:postgres@postgres:5432/feedback"

engine = create_async_engine(DATABASE_URL)

async_session = async_sessionmaker(engine, expire_on_commit=False)
async_session_factory = async_session

Base = declarative_base()

async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
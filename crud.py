import asyncio 
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, User, Profile, Post 

async def create_user(session: AsyncSession, username: str) -> User:
    """Create a new user."""
    user = User(username=username)
    session.add(user)
    await session.commit()
    print(f"Created user: {user}")
    return user


async def main():
    async with db_helper.session_factory() as session:
        await create_user(session, "testuse")
        await create_user(session, "penis")

if __name__ == "__main__":
    asyncio.run(main())
import asyncio 
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, User, Profile, Post 

async def create_user(session: AsyncSession, username: str) -> User:
    """Create a new user."""
    user = User(username=username)
    session.add(user)
    await session.commit()
    print(f"Created user: {user}")
    return user

async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user : User | None = await session.scalar(stmt)
    print(f"Found user: {user}")
    return user

async def create_user_profile(
        session: AsyncSession,
        user_id: int,
        first_name:str | None,
        last_name:str | None,
        ) -> Profile:
    profile = Profile(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
    )
    session.add(profile)    
    await session.commit()


async def create_posts(
        session: AsyncSession,
        user_id: int,
        *posts_titles: str,
        ) -> list[Post]:
    posts = [ 
        Post(title=title, user_id=user_id) for title in posts_titles 
    ]
    session.add_all(posts)    
    await session.commit()
    print(f"Created posts: {posts}")
    return posts

    
async def show_users_with_profiles(session: AsyncSession):
    stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
    users = await session.scalars(stmt)


async def get_users_with_posts(session: AsyncSession):
    stmt = select(User).options(selectinload(User.posts)).order_by(User.id)
    result : Result = await session.execute(stmt)
    users = result.scalars()

    for user in users:
        print(f"User: {user}")
        for post in user.posts:
            print(f"Post: {post}")

async def get_posts_with_authors(session: AsyncSession):
    stmt = select(Post).options(selectinload(Post.user)).order_by(Post.id)
    posts = await session.scalars(stmt)
    for post in posts:
        print(f"post: {post}")

async def main():
    async with db_helper.session_factory() as session:
        # testuser = await get_user_by_username(session=session, username="penis")
        # await create_user_profile(
        #     session=session,
        #     user_id=testuser.id,
        #     first_name="pen",
        #     last_name="altu",
        # )
        # await show_users_with_profiles(session=session)
        # await create_posts(
        #     session,
        #     testuser.id,
        #     "penis1",
        #     "penis2",
        # )
        await get_posts_with_authors(session=session)
if __name__ == "__main__":
    asyncio.run(main())
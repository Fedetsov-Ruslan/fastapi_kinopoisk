from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.users.models import User
from src.movies.models import UserMovies


async def orm_add_favorite(session: AsyncSession, user_id: int, movie_id: str):
    try:
        movie = UserMovies(user_id=user_id, movie_id=movie_id)
        session.add(movie)
        await session.commit()
        return {
            "message": "Favorite added successfully"
            }
    except:
        return {
            "message": "Favorite not added"
            }



from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.users.models import User
from src.movies.models import UserMovies, Movies


async def orm_add_favorite(
    session: AsyncSession,
    user_id: int,
    movie_id: str
):
    try:
        movie = UserMovies(user_id=user_id, movie_id=str(movie_id))
        session.add(movie)
        await session.commit()
        return {
            "message": "Favorite added successfully"
            }
    except:
        return {
            "message": "Favorite not added"
            }
        

async def orm_delete_favorite_movie(
    session: AsyncSession,
    user_id: int,
    movie_id: str
):
    try:
        query = select(UserMovies).where(
            UserMovies.user_id == user_id,
            UserMovies.movie_id == movie_id
            )
        result = await session.execute(query)
        movie = result.scalars().first()
        await session.delete(movie)
        await session.commit()
        return {
            "message": "Favorite deleted successfully"
            }
    except:
        return {
            "message": "kinopoisk_id not found"
            }
        
        
async def orm_get_all_favorites_movies(session: AsyncSession, user_id: int):
    query = select(UserMovies.user_id,
                   Movies).join(Movies).where(UserMovies.user_id == user_id)
    result = await session.execute(query)
    movies_list = []
    for row in result:
        movie = row._asdict()
        movies_list.append({
            "user_id": movie["user_id"],
            "movie_id": movie["Movies"].kinopoisk_id,
            "title": movie["Movies"].title,
            "year": movie["Movies"].year,
            "description": movie["Movies"].description,
            "poster": movie["Movies"].poster,
            "rating": movie["Movies"].rating,
            "rating_kinopoisk": movie["Movies"].rating_kinopoisk,
            "rating_imdb": movie["Movies"].rating_imdb,
            "movie_length": movie["Movies"].movie_length
        }
        )
    return movies_list


async def orm_add_movie(
    session: AsyncSession,
    kinopoisk_id: int,
    title: str,
    year: int,
    description: str,
    poster: str,
    rating: int,
    rating_kinopoisk: int,
    rating_imdb: int,
    movie_length: int
):
    query = select(Movies).where(Movies.kinopoisk_id == kinopoisk_id)
    result = await session.execute(query)
    movie = result.scalars().first()
    if not movie:
        movie = Movies(
            kinopoisk_id=kinopoisk_id,
            title=title,
            year=year,
            description=description,
            poster=poster,
            rating=rating,
            rating_kinopoisk=rating_kinopoisk,
            rating_imdb=rating_imdb,
            movie_length=movie_length
        )
        session.add(movie)
        await session.commit()
    return movie



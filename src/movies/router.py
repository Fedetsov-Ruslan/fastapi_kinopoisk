import aiohttp
import jwt

from fastapi import APIRouter, HTTPException, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.movies.orm_query import orm_add_favorite
from src.database import get_async_session
from src.config import KINOPOISK_API_KEY, SECRET_AUTH


router = APIRouter(
    prefix="/movies",
    tags=["movies"],
)

async def get_session(request: Request):
    return request.app.state.session 

async def get_access_token(
    request: Request
):
    coocke = request.cookies.get("access_token")
    if coocke is None:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated.",
            headers={"WWW-Authenticate": "Bearer"},  
        )
    else:
        return coocke    
    

async def get_movie_for_id(
    id: int,
    api_key: str,
    session: aiohttp.ClientSession = Depends(get_session),
):
    async with session.get(
        url=f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{id}',
        headers={'X-API-KEY': api_key,
        'Content-Type': 'application/json',
    }
    ) as response:
        print(response)
        if response.status != 200:
            raise HTTPException(status_code=response.status, detail="Error fetching data")
        movie_data = await response.json()
    return movie_data
    


@router.get("/{id}")
async def get_movie_for_id(
    id: int,
    current_user: str = Depends(get_access_token),
    session: aiohttp.ClientSession = Depends(get_session)
):
    movie_data = await get_movie_for_id(id, KINOPOISK_API_KEY, session)
    return movie_data


@router.get("/search")
async def get_movie_for_name(
    search: str,
    current_user: str = Depends(get_access_token),
    session: aiohttp.ClientSession = Depends(get_session)
):
    async with session.get(
    url='https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword',
    params={'keyword': search}, 
    headers={
        'X-API-KEY': KINOPOISK_API_KEY,
        'Content-Type': 'application/json',
    }
) as response:
        print(response)
        if response.status != 200:
            raise HTTPException(status_code=response.status, detail="Error fetching data")
        movie_data = await response.json()
    return movie_data


@router.post("/favorites")
async def add_favorites(
    movie_id: int,
    current_user: str = Depends(get_access_token),
    session_db: AsyncSession = Depends(get_async_session),
    session: aiohttp.ClientSession = Depends(get_session)
):
    movie = get_movie_for_id(movie_id, KINOPOISK_API_KEY, session) 
    user = jwt.decode(current_user.encode(), SECRET_AUTH, algorithms=["HS256"], audience=["fastapi-users:auth"])
    query = orm_add_favorite(session_db, int(user["sub"]), str(movie_id))
    return query




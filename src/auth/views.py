import jwt

from fastapi import (
    APIRouter,
    Depends,
    Form,
    HTTPException,
    Response
)


from fastapi import APIRouter, Depends,  HTTPException
from fastapi_users.password import Argon2Hasher
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.auth.orm_query import (
    orm_get_add_user,
    orm_get_user,
    orm_get_user_data
)
from src.auth.schemas import LoginData
from src.auth.base_config import  get_jwt_strategy
from src.config import SECRET_AUTH
from src.auth.auth_jwt import get_access_token



router = APIRouter(prefix="/auth", tags=["auth"])

jwt_strategy = get_jwt_strategy()  


@router.post("/login")
async def login(
    data: LoginData,
    response: Response,
    session: AsyncSession = Depends(get_async_session),
):
    user = await orm_get_user(session, data.username)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail ="not authenticated"
        )
    elif Argon2Hasher().verify(data.password, user.pasword_hash):
        token = await jwt_strategy.write_token(user)
        
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,  
            max_age=360,       
            samesite="Lax"  
        )
        user_dict = {
            "id": user.id,
            "username": user.username,
            "password_hash": user.pasword_hash
        }
        
        return  {"message": "login success"} 
    else:
        raise HTTPException(
            status_code=401,
            detail ="not authenticated"
        )

    
@router.post("/register/")
async def auth_login(
    username: str = Form(),
    password: str = Form(),
    session: AsyncSession = Depends(get_async_session)
):
    result = await orm_get_add_user(session, username, password)
    return {
        "msg": result["message"],
        "username": result["username"]
    }


@router.get("/profile")
async def get_profile(
    current_user: str = Depends(get_access_token),
     session: AsyncSession = Depends(get_async_session)
):
    user = jwt.decode(current_user.encode(), SECRET_AUTH, algorithms=["HS256"], audience=["fastapi-users:auth"])
    user_date = await orm_get_user_data(session, int(user["sub"]))
    return {
        "id": user_date.id,
        "username": user_date.username
    }

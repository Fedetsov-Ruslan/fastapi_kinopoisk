import jwt

from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import (
    HTTPException,
    Response,
    Request
)

from src.config import SECRET_AUTH


def refresh_token(
    user: str,
    response: Response, 
    lifetime_seconds: Optional[int] = 30000000
):
    data = {"sub": str(user.id), "aud": ["fastapi-users:auth"], "type": "refresh"}
    payload = data.copy()
    if lifetime_seconds:
        expire = datetime.now(timezone.utc) + timedelta(seconds=lifetime_seconds)
        payload["exp"] = expire
    refresh_token = jwt.encode(payload, SECRET_AUTH, algorithm="HS256")
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,  
        max_age=lifetime_seconds,
        secure=True  
    )
    return refresh_token
    
    
def get_refresh_token(
    request: Request
):
    coocke = request.cookies.get("refresh_token")
    if coocke is None:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        return coocke


def get_access_token(
    request: Request
):
    coocke = request.cookies.get("access_token")
    if coocke is None:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated. Get access token, on refresh tocken",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        return coocke 
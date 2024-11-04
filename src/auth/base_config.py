from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, CookieTransport, JWTStrategy

from src.auth.manager import get_user_manager
from src.config import SECRET_AUTH, LIFESPAN_ACCESS_TOKEN
from src.users.models import User

cookie_transport = CookieTransport(cookie_name="bounds", cookie_max_age=LIFESPAN_ACCESS_TOKEN)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=LIFESPAN_ACCESS_TOKEN)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
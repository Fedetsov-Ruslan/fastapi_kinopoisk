from fastapi_users.password import Argon2Hasher


def hash_password(
    password: str
) -> bytes:
    return Argon2Hasher().hash(password)


def validate_password(
    password: str,
    hashed_password: bytes  
) -> bool:
    print(hashed_password)
    print(password)
    print(hash_password(password))
    return Argon2Hasher().verify(password, hashed_password)
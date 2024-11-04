import os

from dotenv import load_dotenv

env_vars_to_clear = [
    'DB_NAME',
    'DB_USER',
    'DB_PASS',
    'DB_HOST',
    'DB_PORT',
    'SECRET_AUTH',
    'LIFESPAN_ACCESS_TOKEN',
    'KINOPOISK_API_KEY'
]

for var in env_vars_to_clear:
    os.environ.pop(var, None)

load_dotenv()

DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
SECRET_AUTH=os.getenv("SECRET_AUTH")
LIFESPAN_ACCESS_TOKEN = int(os.getenv("LIFESPAN_ACCESS_TOKEN"))
KINOPOISK_API_KEY=os.getenv("KINOPOISK_API_KEY")


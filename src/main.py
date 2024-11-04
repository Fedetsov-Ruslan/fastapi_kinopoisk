import aiohttp

from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.auth.views import router as auth_router
from src.movies.router import router as movies_router



app = FastAPI()

@app.on_event("startup")
async def startup_event():
    app.state.session = aiohttp.ClientSession()


@app.on_event("shutdown")
async def shutdown_event():
    await app.state.session.close()


app.include_router(auth_router)
app.include_router(movies_router)
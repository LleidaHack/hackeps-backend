from fastapi import FastAPI

from .routers import auth_router, teams_router, users_router

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(teams_router.router)
app.include_router(users_router.router)

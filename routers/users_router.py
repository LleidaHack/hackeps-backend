from fastapi import FastAPI

router = FastAPI(prefix="/users",
        tags=["users"],
        responses={404: {"description": "User/s not found"}},
    )
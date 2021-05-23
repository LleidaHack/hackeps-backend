from fastapi import FastAPI

router = FastAPI(prefix="/auth",
        tags=["auth"],
        responses={404: {"description": "Username not found"}},
    )
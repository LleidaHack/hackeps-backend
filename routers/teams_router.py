from fastapi import FastAPI

router = FastAPI(prefix="/teams",
        tags=["teams"],
        responses={404: {"description": "Team/s not found"}},
    )
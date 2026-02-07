from fastapi import APIRouter

router = APIRouter()


@router.post("/auth/login")
def login() -> dict:
    return {"token": "dev-token"}

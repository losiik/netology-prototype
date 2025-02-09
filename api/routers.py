from fastapi import APIRouter

from api.endpoints.calculator import calculator_router

api_router = APIRouter()
api_router.include_router(calculator_router)

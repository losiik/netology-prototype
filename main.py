import os
from dotenv import load_dotenv


if os.path.exists('.env'):
    load_dotenv('.env')


import uvicorn
from fastapi import FastAPI

from common.settings import settings

from api.routers import api_router

app = FastAPI(openapi_prefix="/api/v1")

app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app, port=settings.port)

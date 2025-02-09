import os
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # base app settings
    port: int = os.getenv("PORT")

    allow_operations: List[str] = ['+', '-', '/', '*']


settings = Settings()

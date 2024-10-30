from fastapi import FastAPI, Depends
import os
from functools import lru_cache
from typing_extensions import Annotated
from uvicorn import Config, Server
from conf import Settings

app = FastAPI()

@lru_cache
def get_settings():
    return Settings()

@app.get("/")
async def root(settings: Annotated[Settings, Depends(get_settings)]):
    port = os.environ.get("PORT", settings.port_number)
    return f'Hello {port}'
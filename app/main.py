from fastapi import FastAPI
from app.api import routes_status

app = FastAPI()

app.include_router(routes_status.router)

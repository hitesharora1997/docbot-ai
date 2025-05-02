from fastapi import FastAPI
from app.api import router

app = FastAPI(title="DocBot AI")
app.include_router(router)
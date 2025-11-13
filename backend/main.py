# backend/main.py

from fastapi import FastAPI
from backend.api.routes_sports import router as sports_router
from backend.api.routes_market import router as market_router

app = FastAPI()

# Regisztráljuk az endpointokat
app.include_router(sports_router, prefix="/sports", tags=["sports"])
app.include_router(market_router, prefix="/market", tags=["market"])

# Indítási logika, például:
@app.get("/")
def read_root():
    return {"message": "AI Data Mining API - Tippmester AI Fusion 1.0"}

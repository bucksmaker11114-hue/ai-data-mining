# backend/api/routes_market.py

from fastapi import APIRouter
from backend.core.market_model import MarketModel

router = APIRouter()
market_model = MarketModel()

@router.post("/market/collect")
def collect_market_data(data: dict):
    """Tőzsdei adatok felvétele"""
    market_model.collect_market_data(data["asset_id"], data["ohlcv"], data["liquidity_data"])
    return {"status": "success"}

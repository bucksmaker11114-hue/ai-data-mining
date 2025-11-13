# backend/api/routes_sports.py

from fastapi import APIRouter
from backend.core.sport_model import SportModel

router = APIRouter()
sport_model = SportModel()

@router.post("/sports/collect")
def collect_sport_data(data: dict):
    """Mérkőzés és sportfogadási adatok felvétele"""
    sport_model.collect_sport_data(data["match_id"], data["xg_home"], data["xg_away"], data["team_stats"], data["odds"])
    return {"status": "success"}

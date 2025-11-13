# backend/core/market_model.py

from datetime import datetime

class MarketModel:
    def __init__(self):
        self.market_data = []  # Piaci adatgyűjtés
        self.assets = []  # Eszközök és coin információk

    def collect_market_data(self, asset_id, ohlcv, liquidity_data):
        """Tőzsdei adatgyűjtés és tárolás"""
        market_entry = {
            "asset_id": asset_id,
            "ohlcv": ohlcv,
            "liquidity_data": liquidity_data,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.market_data.append(market_entry)
        
    def clean_data(self):
        """Outlierek és hibás árak szűrése"""
        for entry in self.market_data:
            if entry["ohlcv"]["close"] < 0:  # Hibás ár szűrése
                entry["ohlcv"]["close"] = 0

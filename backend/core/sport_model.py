# backend/core/sport_model.py

from datetime import datetime

class SportModel:
    def __init__(self):
        self.match_data = []  # Tárolja a mérkőzésadatokat
        self.teams = []  # Csapat statisztikák

    def collect_sport_data(self, match_id, xg_home, xg_away, team_stats, odds):
        """Sportfogadási adatok rögzítése és tárolása"""
        match_entry = {
            "match_id": match_id,
            "xG_home": xg_home,
            "xG_away": xg_away,
            "team_stats": team_stats,
            "odds": odds,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.match_data.append(match_entry)
        
    def clean_data(self):
        """Hiányzó vagy hibás adatok kezelése"""
        for entry in self.match_data:
            if not entry.get("xG_home"):
                entry["xG_home"] = entry["team_stats"]["average_xg"]
            if not entry.get("xG_away"):
                entry["xG_away"] = entry["team_stats"]["average_xg"]

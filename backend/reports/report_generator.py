# backend/reports/report_generator.py
import pandas as pd
from datetime import datetime
import os

def generate_report(df: pd.DataFrame, report_dir: str = "reports", report_name: str = None):
    """
    Egyszerű riport generálás CSV formátumban.
    Ha nincs név megadva, automatikusan generál egy timestamp alapút.
    """
    if df is None or df.empty:
        print("[ReportGenerator] Üres DataFrame, nincs mit menteni.")
        return None

    os.makedirs(report_dir, exist_ok=True)

    if report_name is None:
        report_name = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    file_path = os.path.join(report_dir, report_name)
    try:
        df.to_csv(file_path, index=False)
        print(f"[ReportGenerator] Riport mentve ide: {file_path}")
        return file_path
    except Exception as e:
        print(f"[ReportGenerator] Hiba a riport mentésekor: {e}")
        return None


if __name__ == "__main__":
    # Tesztfutás
    data = {"match": ["Team A - Team B"], "odds": [2.1], "ev": [0.15]}
    df = pd.DataFrame(data)
    generate_report(df)

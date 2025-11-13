# backend/processor/deep_cleaner.py
import pandas as pd

def deep_clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tisztítja a DataFrame-et: duplikátumok, hibás értékek, NaN stb.
    """
    if df is None or df.empty:
        return df

    try:
        # Alapvető tisztítási lépések
        df = df.drop_duplicates()
        df = df.replace(["-", "N/A", "null"], pd.NA)
        df = df.fillna(method="ffill").fillna(method="bfill")

        # Negatív gólok, pontok kizárása
        if "goals" in df.columns:
            df = df[df["goals"] >= 0]

        # Hibás időpontok kiszűrése
        if "date" in df.columns:
            df = df[pd.to_datetime(df["date"], errors="coerce").notna()]

        return df

    except Exception as e:
        print(f"[DeepCleaner] Hiba a tisztítás közben: {e}")
        return df

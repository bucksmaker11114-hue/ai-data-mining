from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai.core_engine import analyze_market, generate_signal
from ai.liquidity_grab import detect_liquidity_grab
from utils.logger import log_trade
import os, datetime, csv, random

app = FastAPI(title="MZ/X 4.3 Self-Learning AI Engine")

# --- Mappák biztosítása ---
os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REPORT_PATH = "reports/daily_log.csv"

# --- Health check ---
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "version": "4.3",
        "time": datetime.datetime.now().isoformat(),
        "mode": os.getenv("AI_MODE", "self_learning"),
    }


# --- Elemzés végrehajtása (liquidity grab integrációval) ---
@app.get("/api/analyze/{pair}")
async def analyze(pair: str):
    """
    Fő elemző endpoint:
    - Meghívja az AI motort (core_engine)
    - Felméri a likviditás állapotát külön
    - Naplózza az eredményt
    """
    # 1️⃣ Futtatás a fő AI motoron keresztül
    result = analyze_market(pair)

    # 2️⃣ Szintetikus árfolyamsor a liquidity vizsgálathoz
    prices = [random.uniform(20000, 60000) if "BTC" in pair.upper() else random.uniform(1000, 4000) for _ in range(20)]
    highs = [p * random.uniform(1.002, 1.006) for p in prices]
    lows = [p * random.uniform(0.994, 0.998) for p in prices]
    closes = prices
    liquidity_state = detect_liquidity_grab(highs, lows, closes)

    # 3️⃣ Kiterjesztett eredmény
    result["liquidity_state"] = liquidity_state

    # 4️⃣ Logolás CSV-be
    log_trade(pair, result)

    # 5️⃣ Visszaküldés a kliensnek
    return {
        "pair": result["pair"],
        "decision": result["decision"],
        "bias": result["bias"],
        "prediction": result["prediction"],
        "structure": result["structure"],
        "liquidity": result["liquidity_state"],
        "risk": result["risk"],
        "time": result["time"]
    }


# --- Gyors jelzés generálása ---
@app.get("/api/signal/{pair}")
async def signal(pair: str):
    return generate_signal(pair)


# --- Jelentés lekérése (CSV) ---
@app.get("/api/report")
async def report():
    try:
        with open(REPORT_PATH, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
            return data[-15:] if data else []
    except FileNotFoundError:
        return {"error": "Nincs még jelentés generálva."}


# --- Gyökér útvonal ---
@app.get("/")
def home():
    return {"message": "MZ/X Backend fut", "AI": "aktív", "liquidity_check": True}

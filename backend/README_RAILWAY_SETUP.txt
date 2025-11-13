🚀 AI Data Mining 2.0 Fusion Intelligence Engine - Railway Telepítési Útmutató

1️⃣ Nyisd meg a Railway-t és hozz létre egy új projektet.

2️⃣ Csatold a GitHub-repót vagy töltsd fel ezt a mappát ZIP formában.

3️⃣ Ellenőrizd, hogy a root mappában ez a struktúra megvan:
   AI Data Mining 2.0 Fusion Intelligence Engine/backend/

4️⃣ A Railway automatikusan felismeri a Procfile-t és a runtime.txt-t.
   Futtatási parancs: 
   uvicorn backend.api.server:app --host 0.0.0.0 --port $PORT

5️⃣ Állítsd be a cron jobot (6 óránként futtatja az adatgyűjtést):

   ```bash
   railway cron add "python backend/main.py" --schedule "0 */6 * * *"

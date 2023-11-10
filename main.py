# Per far funzionare il progetto, assicurarsi di installare tutte le librerie
# Tutti i path sono riferiti alla macchina con la quale è stata sviluppata l'applicazione



# Per mantenere un certo ordine generale nel progetto, ho deciso di modularizzare, per quanto possibile, tutto il codice.
# Ho quindi deciso di evitare di importare tutte le api (del modello e del db) nel file main.py ed ho considerato il main.py come modulo principale per gestire le route dei file api
# Ho pertanto importato le api come moduli, in maniera tale che eseguendo il main.py tutte le API venissero esposte senza dover spostarsi nella cartella in cui sono contenuti i rispettivi file api.py
# Il comando è --> uvicorn main:app --reload

# Importazione delle librerie necessarie
from fastapi import FastAPI
from uvicorn import run
from modello.api import app as model_app
from DB.api import app as db_app

app = FastAPI()

# Comando che monta l'API del modello e lo espone al seguente URL:
# Per Swagger --> (http://127.0.0.1:8000/modello/docs#/)
app.mount("/modello", model_app)

# Comando che monta le API CRUD che si interfacciano con il db, instradate nell'URL in /db
# Per Swagger --> (http://127.0.0.1:8000/db/docs#)
app.mount("/db", db_app)

if __name__ == '__main__':
# Runna il server uvicorn alla porta 8000
    run(app, host="0.0.0.0", port=8000)


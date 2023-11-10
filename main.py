# Per far funzionare il progetto, assicurarsi di installare tutte le librerie
# Tutti i path sono riferiti alla macchina con la quale è stata sviluppata l'applicazione


# Importazione delle librerie necessarie
# Per mantenere un certo ordine generale nel progetto, ho deciso di modularizzare, per quanto possibile, tutto il codice.
# Ho quindi deciso di evitare di importare tutte le api (del modello e del db) nel file main.py ed ho considerato il main.py come route principale per far partire tutte le api
# Ho pertanto importato le api come modello in maniera tale da lanciare contemporaneamente i due file api.py instradandole in due porte differenti per non creare problemi
# Così facendo si può lanciare il server uvicorn direttamente dal file main.py della cartella principale (senza che si debba andare sulla cartella specifica per far partire uvicorn)
# Il comando è --> uvicorn main:app --reload

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


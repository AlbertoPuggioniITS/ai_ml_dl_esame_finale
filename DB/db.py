# importazione delle librerie necessarie
import pandas as pd
import sqlite3
import requests
from io import StringIO

# Importazione dell'URL del wine_data.csv
df_url = 'https://raw.githubusercontent.com/AlbertoPuggioniITS/ai_ml_esame_finale/master/CSV/wine_data.csv'
response_df = requests.get(df_url)
# Check per vedere che la GET mi dia i risultati dall'URL
if response_df.status_code == 200:
    # Importo il csv e leggo i dati
    df_wine = pd.read_csv(StringIO(response_df.text), sep=',')

    # Inserisco il percorso completo nella variabile db_path per la connessione con il db
    db_path = '/Users/albertopuggioni/PycharmProjects/ai_ml_esame_finale/DB/sqlite/wine.db'

    # Creo la connessione con il db e importo il df
    conn = sqlite3.connect(db_path)
    df_wine.to_sql('wine', conn, index=False, if_exists='replace')
    conn.close()
# Messaggio di errore se i dati non sono stati importati
else:
    print('Errore. Status Code:', response_df.status_code)

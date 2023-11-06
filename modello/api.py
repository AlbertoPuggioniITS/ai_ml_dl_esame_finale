# Spostarsi nella cartella modello
#  uvicorn api:app --host 0.0.0.0 --port 8000

# Swagger per il testing dell'API -->  http://0.0.0.0:8000/docs#/

# Importazione delle librerie necessarie
import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

# Creazione del BaseModel basato sulle features del modello
class WineQualityPredictionInput(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float
    quality: int = Field(..., ge=0, le=10)      # ho inserito un check per fare in modo che la 'quality' rientri nei valori compresi tra 0 e 10

# Importazione del modello addestrato
model = joblib.load("/Users/albertopuggioni/PycharmProjects/ai_ml_esame_finale/modello/modello_logistic_regression.pkl")

# API Post - definizione della route, definizione degli input per le features sulle quali il modello farà la previsione
@app.post("/predict_wine_quality/")
def predict_wine_quality(input_data: WineQualityPredictionInput):
    # Elenco delle features utilizzate dal modello
    input_features = [
        input_data.fixed_acidity,
        input_data.volatile_acidity,
        input_data.citric_acid,
        input_data.residual_sugar,
        input_data.chlorides,
        input_data.free_sulfur_dioxide,
        input_data.density,
        input_data.pH,
        input_data.sulphates,
        input_data.alcohol,
        input_data.quality
    ]

    # Previsioni utilizzando il modello
    # Ulteriore check per controllare che l'utente inserisca solo gli input utili al modello
    # Predizione: 0 pessima qualità, 1 ottima qualità
    if len(input_features) == 11:
        prediction = model.predict([input_features])
        return {"Predizione: "
                "[0: pessima qualità / 1: ottima qualità]": prediction.tolist()}
    else:
        return {"Errore": "Il numero di features nell'input non corrisponde al modello addestrato."}

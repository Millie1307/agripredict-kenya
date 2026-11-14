from fastapi import FastAPI
from backend.app.routes import crops, livestock, weather, markets

app = FastAPI(
    title="AgriPredict Kenya API",
    description="Agricultural intelligence and prediction platform for Kenya.",
    version="1.0.0"
)

app.include_router(crops.router)
app.include_router(livestock.router)
app.include_router(weather.router)
app.include_router(markets.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AgriPredict Kenya!",
        "status": "running",
        "platform": "Agricultural Intelligence and Prediction"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AgriPredict Kenya API"
    }
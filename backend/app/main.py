from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.request import MatchRequest
from app.schemas.response import PredictionResponse
from app.service.prediction_service import predict_match
from app.api.metadata import router as metadata_router

app = FastAPI(
    title="IPL Analytics Platform API",
    description="AI-powered IPL Match Winner Prediction API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(metadata_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to IPL Analytics Platform 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: MatchRequest):
    return predict_match(request)
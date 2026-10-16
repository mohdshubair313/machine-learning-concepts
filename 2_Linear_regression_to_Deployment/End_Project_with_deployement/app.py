import pickle
from pathlib import Path
from typing import Dict, Any

import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field

# -------------------------------------------------------------
# Base Directories & Model Loading
# -------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"
TEMPLATES_DIR = BASE_DIR / "templates"

scaler_path = MODELS_DIR / "scaler.pkl"
model_path = MODELS_DIR / "House_Price_model.pkl"

if not scaler_path.exists() or not model_path.exists():
    raise FileNotFoundError(
        f"Missing model files in {MODELS_DIR}. Ensure scaler.pkl and House_Price_model.pkl exist."
    )

with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

with open(model_path, "rb") as f:
    model = pickle.load(f)

# The exact 20 feature names in the order expected by the scaler
FEATURE_NAMES = [
    'number of bedrooms',
    'number of bathrooms',
    'living area',
    'lot area',
    'number of floors',
    'waterfront present',
    'number of views',
    'condition of the house',
    'grade of the house',
    'Area of the house(excluding basement)',
    'Area of the basement',
    'Built Year',
    'Renovation Year',
    'Postal Code',
    'Lattitude',
    'Longitude',
    'living_area_renov',
    'lot_area_renov',
    'Number of schools nearby',
    'Distance from the airport'
]

# -------------------------------------------------------------
# FastAPI App Initialization
# -------------------------------------------------------------
app = FastAPI(
    title="ProphetHomes AI Engine",
    description="Production-ready FastAPI valuation engine using Scikit-Learn RidgeCV & StandardScaler",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------------------------------------
# Pydantic Schemas
# -------------------------------------------------------------
class HouseFeatures(BaseModel):
    bedrooms: float = Field(3.0, ge=1, le=33, description="Number of bedrooms")
    bathrooms: float = Field(2.25, ge=0.5, le=10, description="Number of bathrooms")
    living_area: float = Field(1930.0, ge=200, description="Living area in sq. ft.")
    lot_area: float = Field(7620.0, ge=200, description="Lot/Plot area in sq. ft.")
    floors: float = Field(1.5, ge=1.0, le=4.0, description="Number of floors")
    waterfront: int = Field(0, ge=0, le=1, description="Waterfront present (0 = No, 1 = Yes)")
    views: int = Field(0, ge=0, le=4, description="View quality rating (0 to 4)")
    condition: int = Field(3, ge=1, le=5, description="House condition (1 to 5)")
    grade: int = Field(7, ge=1, le=13, description="Construction grade (1 to 13)")
    area_excluding_basement: float = Field(1580.0, ge=200, description="Area excluding basement in sq. ft.")
    area_basement: float = Field(0.0, ge=0, description="Basement area in sq. ft.")
    built_year: int = Field(1975, ge=1900, le=2026, description="Year built")
    renovation_year: int = Field(0, ge=0, le=2026, description="Year renovated (0 if never)")
    postal_code: int = Field(122032, description="Postal code zone")
    latitude: float = Field(52.8064, description="Lattitude coordinate")
    longitude: float = Field(-114.421, description="Longitude coordinate")
    living_area_renov: float = Field(1850.0, ge=200, description="Living area renovated")
    lot_area_renov: float = Field(7620.0, ge=200, description="Lot area renovated")
    schools_nearby: int = Field(2, ge=0, le=10, description="Number of schools nearby")
    distance_airport: float = Field(65.0, ge=0, description="Distance from airport in km")


# -------------------------------------------------------------
# Utility: Currency Formatting
# -------------------------------------------------------------
def format_inr(amount: float) -> str:
    """Format floating point numbers into Indian currency style (e.g. ₹ 4,01,633)."""
    amt_int = int(round(amount))
    s = str(amt_int)
    if len(s) <= 3:
        formatted = s
    else:
        last3 = s[-3:]
        rest = s[:-3]
        groups = []
        while len(rest) > 2:
            groups.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            groups.insert(0, rest)
        formatted = ",".join(groups) + "," + last3
    return f"₹ {formatted}"


def format_inr_words(amount: float) -> str:
    """Format numbers into readable Lakhs / Crores string."""
    if amount >= 10000000:
        cr = amount / 10000000
        return f"₹ {cr:.2f} Crores"
    elif amount >= 100000:
        lakhs = amount / 100000
        return f"₹ {lakhs:.2f} Lakhs"
    else:
        return format_inr(amount)


# -------------------------------------------------------------
# Routes
# -------------------------------------------------------------
@app.get("/", response_class=FileResponse)
async def serve_home():
    """Serves the interactive high-aesthetic web interface."""
    html_file = TEMPLATES_DIR / "index.html"
    if not html_file.exists():
        raise HTTPException(status_code=404, detail="Frontend template not found.")
    return FileResponse(html_file)


@app.post("/predict")
async def predict_price(features: HouseFeatures):
    """
    Predicts house valuation using the standardized pipeline:
    Raw Features -> StandardScaler (scaler.pkl) -> RidgeCV (House_Price_model.pkl).
    """
    try:
        # Map pydantic payload to exact column dictionary
        input_dict = {
            'number of bedrooms': features.bedrooms,
            'number of bathrooms': features.bathrooms,
            'living area': features.living_area,
            'lot area': features.lot_area,
            'number of floors': features.floors,
            'waterfront present': features.waterfront,
            'number of views': features.views,
            'condition of the house': features.condition,
            'grade of the house': features.grade,
            'Area of the house(excluding basement)': features.area_excluding_basement,
            'Area of the basement': features.area_basement,
            'Built Year': features.built_year,
            'Renovation Year': features.renovation_year,
            'Postal Code': features.postal_code,
            'Lattitude': features.latitude,
            'Longitude': features.longitude,
            'living_area_renov': features.living_area_renov,
            'lot_area_renov': features.lot_area_renov,
            'Number of schools nearby': features.schools_nearby,
            'Distance from the airport': features.distance_airport,
        }

        df_input = pd.DataFrame([input_dict], columns=FEATURE_NAMES)

        # Scale using pre-fitted StandardScaler
        scaled_input = scaler.transform(df_input)

        # Predict using RidgeCV
        predicted_raw = float(model.predict(scaled_input)[0])

        # Floor prediction to 0 to prevent negative values on extreme outliers
        final_price = max(0.0, predicted_raw)

        return JSONResponse({
            "status": "success",
            "predicted_price_raw": round(final_price, 2),
            "formatted_price": format_inr(final_price),
            "price_in_lakhs": format_inr_words(final_price),
            "model_metadata": {
                "algorithm": "RidgeCV (L2 Regularized Multiple Regression)",
                "validation_r2": 0.6952,
                "features_count": len(FEATURE_NAMES)
            }
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint to verify model readiness."""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "scaler_loaded": scaler is not None,
        "total_features": len(FEATURE_NAMES)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

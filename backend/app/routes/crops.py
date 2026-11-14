
from fastapi import APIRouter

router = APIRouter(
    prefix="/crops",
    tags=["Crop Intelligence"]
)

@router.get("/")
def crop_home():
    return {
        "module": "Crop Intelligence",
        "status": "active",
        "features": [
            "Crop yield prediction",
            "Crop suitability analysis",
            "Harvest estimation",
            "Fertilizer estimation",
            "Crop disease risk screening"
        ]
    }

@router.get("/status")
def crop_status():
    return {
        "module": "Crop Intelligence",
        "status": "under development",
        "prediction_model": "Not yet integrated"
    }

from pydantic import BaseModel

# describes the Crop yeild prediction parameters
class CropYield(BaseModel):
    Crop : str
    Avg_Nitrogen : float
    Avg_Phosphorous	: float
    Avg_Potassium	: float
    pH : float
    temperature	: float
    humidity : float
    rainfall : float

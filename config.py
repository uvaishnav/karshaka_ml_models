from pydantic import BaseModel

# describes the crop recomendation parameters
class CropRecomend(BaseModel):
    N : float
    P : float
    K : float
    temperature : float
    humidity : float
    ph : float
    rainfall : float

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

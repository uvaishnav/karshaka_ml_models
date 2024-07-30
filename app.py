# 1. Library imports

import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import joblib

from config import CropYield, CropRecomend
from preprocessor import log_normal_transform 


# 2. Create the app object
app = FastAPI()

# load crop recomendation model
crop_recomendation = joblib.load("models/crop_recomend_model.pkl")


# load preprocessor for yield prediction
preprocessor = joblib.load("models/preprocessor.pkl")

# Load scaler to Normalize the input for crop recomendation
scaler = joblib.load("models/crop_recomend_scaler.pkl")

# yeild prediction model
crop_yeild_prediction = joblib.load("models/best_RandomForest_model.pkl")


@app.get('/')
def index():
    return {'message': 'Karshak Siksha'}

@app.post('/recomendCrop')
def get_crop_recomendation(data: CropRecomend):
    data = data.dict()
    N = data['N']
    P = data['P']
    K = data['K']
    temperature = data['temperature']
    humidity = data['humidity']
    ph = data['ph']
    rainfall = data['rainfall']

    prediction = crop_recomendation.predict([[N,P,K,temperature,humidity,ph,rainfall]])

    if prediction==0:
        prediction = 'banana'
    elif prediction == 1:
        prediction = 'coconut'
    elif prediction == 2:
        prediction = 'jute'
    elif prediction == 3:
        prediction = 'maize'
    elif prediction == 4:
        prediction = 'rice'
    else:
        prediction = 'none'
    
    return{
        'prediction': prediction
    }

@app.post('/predictYeild')
def get_yeild_prediction(data: CropYield):
    # Convert the input data to a dictionary
    data_dict = data.dict()
    
    # Extract individual fields
    Crop = data_dict['Crop']
    Avg_Nitrogen = data_dict['Avg_Nitrogen']
    Avg_Phosphorous = data_dict['Avg_Phosphorous']
    Avg_Potassium = data_dict['Avg_Potassium']
    pH = data_dict['pH']
    temperature = data_dict['temperature']
    humidity = data_dict['humidity']
    rainfall = data_dict['rainfall']
    
    # Create a DataFrame from the input data
    input_data = pd.DataFrame({
        'Crop': [Crop],
        'Avg_Nitrogen': [Avg_Nitrogen],
        'Avg_Phosphorous': [Avg_Phosphorous],
        'Avg_Potassium': [Avg_Potassium],
        'pH': [pH],
        'temperature': [temperature],
        'humidity': [humidity],
        'rainfall': [rainfall]
    })
    
    # Apply the preprocessor to the input data
    processed_data = preprocessor.transform(input_data)
    
    # Make a prediction using the processed data
    prediction = crop_yeild_prediction.predict(processed_data)
    
    # Return the prediction result
    return {
        'prediction': np.exp(prediction[0])
    }

# 5. Run the API with uvicorn
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn app:app --reload
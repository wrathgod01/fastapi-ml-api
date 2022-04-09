import numpy as np
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from assets.item_model import ItemDetails
from assets.transform import transform_data
from assets.load_model import load_model_from_deta_drive

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://wrathgod01.github.io/sales-prediction-frontend/", "localhost:5500/index.html"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/')
def entry_point():
    return { 'message': 'Welcome to Sales Forecasting API !!!' }

@app.get('/params/{param}')
async def get_values_of_attributes(param: str):
    df = pd.read_json('datasets/data.json')
    if param not in ['item_identifier', 'item_fat_content', 'item_type', 'outlet_identifier', 'outlet_size', 'outlet_location_type', 'outlet_type']:
        return { 
            'status': 404,
            'result': 'No such attribute exists' 
        }

    final_list = df['train'][param]
    
    return { 
        'status': 200,
        'length': final_list.strip('][').split(', ').__len__(),
        'result': final_list 
    }




@app.post('/predict')
async def predict_sales(data: ItemDetails):
    data = data.dict()
    
    transformed_data = np.array(transform_data(data))
    
    model = load_model_from_deta_drive()
    predicted_sales = model.predict(transformed_data)    
    
    return {
        'status': 200, 
        'predicted_sales': predicted_sales[0]
    }
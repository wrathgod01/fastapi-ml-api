import uvicorn
import pickle
import numpy as np
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from assets.item_model import ItemDetails
from assets.transform import transform_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

with open("__model__/model.pkl", "rb") as rf:
    model = pickle.load(rf)

@app.get('/')
async def welcome():
    return { 'message': 'Welcome to this API!'}


@app.get('/{page}')
async def get_data(page: int):
    no_of_records_per_page = 10
    start = (no_of_records_per_page * (page-1))
    end = (page * no_of_records_per_page) 

    df = pd.read_csv('datasets/train.csv')
    data = df.iloc[start:end].to_json(orient ='records')

    return { 
        'status': 200,
        'data': data 
    }




@app.get('/params/{param}')
async def get_result_list(param: str):
    df = pd.read_csv('datasets/train.csv')
    attr = ''
    
    if(param == 'item_identifier'): 
        attr = 'Item_Identifier'
    elif(param == 'item_fat_content'):
        attr = 'Item_Fat_Content'
    elif(param == 'item_type'):
        attr = 'Item_Type'
    elif(param == 'outlet_identifier'):
        attr = 'Outlet_Identifier'
    elif(param == 'outlet_size'):
        attr = 'Outlet_Size'
    elif(param == 'outlet_location_type'):
        attr = 'Outlet_Location_Type'
    elif(param == 'outlet_type'):
        attr = 'Outlet_Type'
    else:
        return { 
            'status': 404,
            'result': 'No such attribute exists' 
        }


    final_list = df[attr].unique().tolist()
    
    if(attr == 'Item_Fat_Content'):
        final_list = [e for e in final_list if e != 'LF' and e != 'reg' and e != 'low fat']
    elif(attr == 'Outlet_Size'):
        final_list = [e for e in final_list if str(e) != 'nan']  # To check if it is nan/NAN, it can't be equal to itself

    return { 
        'status': 200,
        'result': final_list 
    }




@app.post('/predict')
async def predict_sales(data: ItemDetails):
    data = data.dict()
    
    transformed_data = np.array(transform_data(data))
    
    predicted_sales = model.predict(transformed_data)    
    
    return {
        'status': 200, 
        'predicted_sales': predicted_sales[0] 
    }


# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)



# python -m uvicorn main:app --reload
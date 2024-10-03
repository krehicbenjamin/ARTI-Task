import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os
import pickle

def predict_regression(input_data):
    script_dir = os.path.dirname(__file__)
   
    model_path = os.path.abspath(os.path.join(script_dir, 'xgboost_regression_model.json'))
    
    print(f"Loading model from: {model_path}")
    
   
    model = xgb.XGBRegressor()
    model.load_model(model_path)
    
   
    scaler_path = os.path.abspath(os.path.join(script_dir, 'xboost_scaler.pkl'))
    print(f"Loading scaler from: {scaler_path}")
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    
    
    feature_names = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
                     'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
                     'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']
    
    
    input_df = pd.DataFrame([input_data], columns=feature_names)
    
    
    input_scaled = scaler.transform(input_df)
    
    
    prediction = model.predict(input_scaled)
    
    
    prediction_original_scale = np.expm1(prediction)
    
    return prediction_original_scale.tolist()
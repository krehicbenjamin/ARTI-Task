import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
import joblib
import pickle


def predict_timeseries(input_data):
    
    if len(input_data) != 10:
        raise ValueError("Input data must have exactly 10 time steps.")
    
    
    script_dir = os.path.dirname(__file__)
    
    
    model_path = os.path.abspath(os.path.join(script_dir, 'timeseries_lstm_model.h5'))
    
    scaler_path = os.path.abspath(os.path.join(script_dir, 'scaler.pkl'))

    
    model = load_model(model_path)

    
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)

    
    input_data = np.array(input_data).reshape(-1, 1)  

    
    scaled_input_data = scaler.transform(input_data)

    
    scaled_input_data = scaled_input_data.reshape(1, 10, 1)  

   
    prediction = model.predict(scaled_input_data)

    
    prediction_original_scale = scaler.inverse_transform(prediction)

    
    return prediction_original_scale.tolist()
# Import Libraries
from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger
from pycaret.regression import *

# Create app framework
app=Flask(__name__)
Swagger(app)

saved_final_lightgbm = load_model('Final LightGBM Model')

@app.route('/')
def welcome():
    return "Hello World! Please go to /apidocs :)"


@app.route('/predict',methods=["POST"])
def predict_note_file():
    """Rossman Model
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    
    result = predict_model(saved_final_lightgbm, df_test)['Label']
    
    return str("Sales Prediction = ") + str(result.values.tolist())

if __name__=='__main__':
  app.run()
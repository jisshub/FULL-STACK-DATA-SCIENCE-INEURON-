# create a flask app to serve the model
from ast import If
import re
from turtle import pd
from urllib import response
from flask import Flask, render_template, request, Response

import pickle
import pandas as pd

# load the model from disk
loaded_model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/predict', methods=['POST'])

def predict_log():
    # load the model from disk
    model = pickle.load(open('model.pkl', 'rb'))
    # prepare dataframe
    data_df = pd.DataFrame(dict, index=[1,])
    # make prediction
    predict = model.predict(data_df)
    return predict

def predictRoute():
    try:
        if request.json['data'] is not None:
            data = request.json['data']
            print('data is:', data)
            response = predict_log(data)
            print('result is:', response)
            return Response(response)
    except ValueError:
        return Response('Error: No data provided')
    except Exception as e:
        print('exception is:', e)
        return Response('Error: ' + str(e))

if __name__ == '__main__':
    app.run(debug=True)
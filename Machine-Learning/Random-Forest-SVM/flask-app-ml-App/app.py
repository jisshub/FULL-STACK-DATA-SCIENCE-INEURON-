from crypt import methods
import pickle
from flask import Flask, request, app, jsonify, url_for
import numpy as np
import pandas as pd

# start flask app
app = Flask(__name__)


# load the pickle file.
model = pickle.load(open('model.pkl', 'rb'))


# create a prediction API
@app.route('/predictions', methods=['POST'])
def predictions():
    data = request.json['data']
    print(data)
    # create a list of dicitonary values
    new_data = [list(data.values())]
    # predict the output using new data.
    output = model.predict(new_data)[0]
    # convert the output to json.
    return jsonify(output)

@app.route('/predict', methods=['POST'])
def predict():
    # get values from form inputs
    data = request.form.values()
    new_data = [list(data.values())]
    output = model.predict(new_data)[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
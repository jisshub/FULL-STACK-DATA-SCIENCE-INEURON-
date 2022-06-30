import pickle
from flask import Flask, request, app, jsonify, url_for, render_template, redirect, flash, session, abort, send_from_directory
import numpy as np
import pandas as pd

# start flask app
app = Flask(__name__)


# load the pickle file.
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')

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


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # get the data from form
    data = [float(x) for x in request.form.values()]

    # convert the data to 2D
    final_features = list(data)
    print(data)

    # print the data and take 0th output
    output = model.predict(final_features)[0]
    print(output)
    #output = round(prediction[0], 2)
    return render_template('home.html', prediction_text="Airfoil pressure is  {}".format(output))


if __name__ == '__main__':
    app.run(debug=True)


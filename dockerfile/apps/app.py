from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

# @app.route('/predict')
# def predict():
# 	 #use entries from the query string here but could also use json
#      age = request.args.get('age')
#      absences = request.args.get('absences')
#      health = request.args.get('health')
#      data = [[age],[health],[absences]]
#      query_df = pd.DataFrame({ 'age' : pd.Series(age) ,'health' : pd.Series(health) ,'absences' : pd.Series(absences)})
#      query = pd.get_dummies(query_df)
#      prediction = clf.predict(query)
#      return jsonify(np.asscalar(prediction))


@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_, index=[0])
    query = pd.get_dummies(query_df)
    prediction = clf.predict(query)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)
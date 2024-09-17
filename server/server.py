from flask import Flask, request, jsonify
from flask_cors import CORS

import util

app = Flask(__name__)
CORS(app, resources={r"/predict_house_price": {"origins": "http://localhost:3000"}})

@app.route('/get_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    city = request.form['city']
    Land_size = float(request.form['Land_size'])
    House_size = float(request.form['House_size'])
    Beds = int(request.form['Beds'])
    Baths = int(request.form['Baths'])

    response = jsonify({
        'estimated_price': float(util.get_estimated_price(city, Land_size, House_size, Beds, Baths))
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



if __name__ == "__main__":
    print("starting python flask server for house price prediction")
    util.load_saved_artifacts()
    app.run()
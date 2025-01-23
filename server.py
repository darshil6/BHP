from bottle import response
from flask import Flask, request, jsonify
from flask_cors import CORS
import util
app = Flask(__name__)
CORS(app)
@app.route('/get_location_name')
def get_location_name():

    response = jsonify({
        'locations': util.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = float(request.form['bhk'])
    bath = float(request.form['bath'])

    response = jsonify({'estimated_price' : util.get_estimated_price(location,total_sqft, bhk, bath)})

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
if __name__ == '__main__':
    print("Server started...")
    util.load_saved_artifact()
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)

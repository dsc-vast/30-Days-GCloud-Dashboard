from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin

# Get the file path
import sys
sys.path.append('../scrapper')
from get import get, getSorted, getNameSorted


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello_world():
  x = get()
  return jsonify(x)

@app.route('/sorted')
def sorted():
    x = getSorted()
    return jsonify(x)

@app.route('/name')
def sortedName():
    x = getNameSorted()
    return jsonify(x)

from flask import Flask
from flask import jsonify

# Get the file path
import sys
sys.path.append('../scrapper')
from get import get

app = Flask(__name__)

@app.route('/')
def hello_world():
  x = get()
  return jsonify(x)

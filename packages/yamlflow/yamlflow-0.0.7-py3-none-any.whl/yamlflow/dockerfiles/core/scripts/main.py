from flask import Flask, request

from service.predictor import Predictor


predictor = Predictor()
app = Flask(__name__)


@app.route('/', methods=['POST'])
def predict():
    payload = request.json
    out = predictor.predict(payload)
    return out

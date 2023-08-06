from flask import Flask, request
from predictor import Predictor


predictor = Predictor()
app = Flask(__name__)


@app.route('/', methods=['POST'])
def predict():
    model_input = predictor.pre_process(request.json)
    model_output = predictor.predict(model_input)
    return predictor.post_process(model_output)

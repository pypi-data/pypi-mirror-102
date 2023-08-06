ARG BACKEND

FROM ml_model_server:${BACKEND}

COPY predictor.py predictor.py

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

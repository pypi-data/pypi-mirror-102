ARG BACKEND

FROM ml_model_server:${BACKEND}

COPY models models

COPY service service

RUN pip install -r service/requirements.txt

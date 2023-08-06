FROM python:3.8-slim

# Update and install common
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install web (server & framework)
RUN pip install --upgrade --no-cache-dir \
    gunicorn \
    flask

# Copy start executable
COPY ./start.sh /start.sh
RUN chmod +x /start.sh

# Copy gunicorn_conf.py
COPY gunicorn_conf.py /gunicorn_conf.py

# Copy main.py
COPY main.py /service/main.py

# Set working directory
WORKDIR /service/

# Run the start script
CMD ["/start.sh"]

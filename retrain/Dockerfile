FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

COPY retrain/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY retrain/ ./retrain/

RUN chmod +x /app/retrain/retrain.sh

CMD ["/app/retrain/retrain.sh"]
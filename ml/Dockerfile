FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

COPY ml/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY ml/ ./ml/

RUN chmod +x /app/ml/combine_train.sh

CMD ["/app/ml/combine_train.sh"]
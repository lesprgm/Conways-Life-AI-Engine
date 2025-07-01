FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]


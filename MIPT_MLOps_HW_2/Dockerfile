FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    git \
    gcc \
    g++ \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY . .

RUN dvc init
RUN dvc remote add -d storage /tmp/dvc-storage
RUN dvc pull --force || echo "DVC pull failed. Ensure remote storage is configured correctly."

CMD ["python3", "src/train.py"]
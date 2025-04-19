FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

RUN apt-get update && apt-get install -y wait-for-it

CMD ["gunicorn", "sklad_api.wsgi:application", "--bind", "0.0.0.0:8000"]

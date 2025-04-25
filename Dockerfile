FROM python:3.12.7-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "auth_api.wsgi:application", "--bind", "0.0.0.0:8000"]

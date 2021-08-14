FROM python:3.7

RUN python -m pip install fastapi httpx scrapy gunicorn uvicorn uvloop httptools redis

WORKDIR /app

ADD cache-few-threads-microservice.py cache-few-threads-microservice.py

FROM python:3.7

RUN python -m pip install fastapi httpx scrapy gunicorn uvicorn uvloop httptools

WORKDIR /app

ADD async-few-threads-microservice.py async-few-threads-microservice.py
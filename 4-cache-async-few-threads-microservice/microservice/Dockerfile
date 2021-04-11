FROM python:3.7

RUN python -m pip install fastapi httpx scrapy gunicorn uvicorn uvloop httptools aioredis

WORKDIR /app

ADD microservice.py microservice.py
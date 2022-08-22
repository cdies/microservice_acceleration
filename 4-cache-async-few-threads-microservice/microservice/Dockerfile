FROM python:3.7

RUN python -m pip install fastapi httpx scrapy gunicorn uvicorn uvloop httptools aioredis==1.3.1

WORKDIR /app

ADD cache-async-few-threads-microservice.py cache-async-few-threads-microservice.py

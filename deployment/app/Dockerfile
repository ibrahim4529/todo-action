FROM python:3.10-slim

WORKDIR /app

COPY ./server_app/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY server_app app


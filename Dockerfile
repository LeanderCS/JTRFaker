FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN python3 -m venv venv
RUN . venv/bin/activate

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app/src

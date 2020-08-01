FROM python:3.8-slim

WORKDIR /api_a

COPY ./requirements.txt /api_a/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /api_a/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /api_a/
# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
FROM python:3-slim

COPY ./app /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql nano \
  && apt-get -y install curl npm cargo \ 
  && apt-get clean \
  && npm install -g --save-dev webpack \
  && npm install -g --save-dev webpack-cli \
  && npm install -g yarn \
  && cd /app/sigma-rust/bindings/ergo-lib-wasm/ 
  # && cargo install wasm-pack \

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD tail /dev/null -f

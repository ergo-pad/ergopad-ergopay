FROM python:3

COPY ./app /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc g++ postgresql nano \
  && apt-get -y install curl openjdk-11-jdk
  # && apt-get -y install npm cargo \ 
  && apt-get clean
# RUN npm install -g --save-dev webpack \
  # && npm install -g --save-dev webpack-cli \
  # && npm install -g yarn \
  # && cd /app/sigma-rust/bindings/ergo-lib-wasm/ 
  # && cargo install wasm-pack \

# install python dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD tail /dev/null -f

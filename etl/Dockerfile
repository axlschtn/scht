FROM ubuntu:latest
LABEL maintainer="Axel Schouten"

# JDK RUN
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

RUN \
    pip install --upgrade pip && \
    pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /etl

COPY . /etl/

RUN touch README.md

RUN poetry install --without dev && rm -rf $POETRY_CACHE_DIR

CMD [ "poetry", "run", "python3", "etl_pyspark.py" ]


FROM python:3.12-slim

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /api/

RUN \
    pip install poetry && \
    touch README.md

COPY ./api /api

RUN chmod +x start.sh

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

CMD ["./start.sh"]
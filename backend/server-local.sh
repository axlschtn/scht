#!/bin/sh
export PORT=${PORT:-8000}
export HOST=${HOST:-0.0.0.0}
poetry run uvicorn src.main:app --host=$HOST --port=$PORT --reload 
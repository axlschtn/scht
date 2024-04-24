#!/bin/sh
export PORT=${PORT:-8000}
export HOST=${HOST:-0.0.0.0}
echo $PORT
echo $HOST
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind $HOST:$PORT
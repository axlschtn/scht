#/bin/sh
poetry run uvicorn src.main:app --host 0.0.0.0 --port $PORT
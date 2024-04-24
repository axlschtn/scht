FROM python:3.12 as python-base
WORKDIR  /app
COPY /pyproject.toml /app
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install 
COPY src /app
COPY /server-prod.sh /app
RUN chmod +x /app/server-prod.sh

CMD ["/app/server-prod.sh"]

FROM python:3.9-slim

WORKDIR /app

COPY ./app /app/app
COPY pyproject.toml /app/

RUN pip install poetry && poetry install

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

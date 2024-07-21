#fastapi dockerfile
FROM python:3.11.7-slim-bookworm

WORKDIR /fastapi

COPY ./requirements.txt /fastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt

COPY ./app /fastapi/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--log-level", "debug"]

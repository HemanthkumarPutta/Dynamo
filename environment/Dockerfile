FROM python:3.11-slim@sha256:b652875ab9d721fa0c201e8a9587501c37d4ea547e171b306b3a010077c44e05

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
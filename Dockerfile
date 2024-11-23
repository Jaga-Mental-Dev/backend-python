FROM python:3.12.3-slim

WORKDIR /app

COPY . .

COPY .env .env

ENV PYTHONUNBUFFERED True
ENV PORT 8080

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT} --workers 1
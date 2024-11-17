FROM python:3.11-bullseye

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8672

ENV PORT=8672

CMD ["gunicorn", "--bind", "0.0.0.0:8672", "run:app"]

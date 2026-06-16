FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV CODEX_HOME=/app/codex-home
ENV REVIEW_CONFIG_PATH=/app/config/projects.json
ENV PYTHONPATH=/app/src

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends git ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY config ./config

RUN mkdir -p /app/state /app/codex-home

CMD ["python", "-m", "codereview_service"]

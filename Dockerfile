ARG PYTHON_BASE_IMAGE=python:3.11-slim-bookworm
FROM ${PYTHON_BASE_IMAGE}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV CODEX_HOME=/app/codex-home
ENV REVIEW_CONFIG_PATH=/app/config/projects.json
ENV PYTHONPATH=/app/src

WORKDIR /app

COPY requirements.txt .
COPY vendor ./vendor
RUN set -eux; \
    if find /app/vendor -maxdepth 1 -type f \( -name '*.whl' -o -name '*.tar.gz' -o -name '*.zip' \) | grep -q .; then \
        python -m pip install --no-index --find-links=/app/vendor -r requirements.txt; \
    else \
        python -m pip install --no-cache-dir -r requirements.txt; \
    fi

COPY src ./src
COPY config ./config

RUN mkdir -p /app/state /app/codex-home

CMD ["python", "-m", "codereview_service"]

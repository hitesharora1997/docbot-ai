# --------------------
# Build
# --------------------
FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ----------------------
# Runtime
# ----------------------
FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY ui .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

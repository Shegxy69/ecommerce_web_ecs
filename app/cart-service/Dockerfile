FROM python:3.12-slim

WORKDIR /app

RUN groupadd -g 10001 appgroup && useradd -u 10001 -g appgroup -m appuser

COPY --chown=root:root --chmod=0444 requirements.lock ./

RUN pip install --no-cache-dir --only-binary :all: --require-hashes -r requirements.lock

COPY --chown=root:root --chmod=0444 main.py ./
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

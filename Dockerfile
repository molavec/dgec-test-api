FROM python:3.10.12 AS base

# Install dependencies only when needed
FROM base AS deps
WORKDIR /api
COPY ./requirements.txt /api/requirements.txt
RUN pip install --no-cache-dir -r /api/requirements.txt
RUN pip list -v


FROM base AS runner
WORKDIR /api

# Copia las dependencias
COPY --from=deps /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copia archivos del proyecto
COPY app /api/app

EXPOSE 8000

# Ejecuta
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dependências de sistema básicas
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalação de dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
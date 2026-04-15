# Base Python 3.12 slim
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Atualiza e instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instala Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_24.x | bash - \
    && apt-get install -y nodejs

WORKDIR /app

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instala dependências Node (Tailwind)
# Copiamos apenas os arquivos de manifesto primeiro para aproveitar o cache do Docker
COPY theme/static_src/package*.json ./theme/static_src/
RUN cd theme/static_src && npm install

# Copia o restante do projeto
COPY . .

EXPOSE 8000
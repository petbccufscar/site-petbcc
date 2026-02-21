#!/bin/bash

VENV_DIR=".venv"

echo "Verificando ambiente virtual..."

# 1. Criar venv caso não exista
if [ ! -d "$VENV_DIR" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv $VENV_DIR
else
    echo "Ambiente virtual já existe."
fi

# 2. Ativar venv
echo "Ativando ambiente virtual..."
source $VENV_DIR/bin/activate

# 3. Atualizar ferramentas base
echo "Atualizando pip, setuptools e wheel..."
pip install --upgrade pip setuptools wheel

# 4. Instalar requirements
if [ -f "requirements.txt" ]; then
    echo "Instalando dependências..."
    pip install -r requirements.txt
else
    echo "requirements.txt não encontrado."
fi

echo "Setup finalizado!"

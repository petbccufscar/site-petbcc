$VenvDir = ".venv"

Write-Host "Verificando ambiente virtual..."

# 1. Criar venv caso não exista
if (!(Test-Path $VenvDir)) {
    Write-Host "Criando ambiente virtual..."
    python -m venv $VenvDir
} else {
    Write-Host "Ambiente virtual já existe."
}

# 2. Ativar venv
Write-Host "Ativando ambiente virtual..."
& ".\.venv\Scripts\Activate.ps1"

# 3. Atualizar pip, setuptools e wheel
Write-Host "Atualizando pip, setuptools e wheel..."
pip install --upgrade pip setuptools wheel

# 4. Instalar dependências
if (Test-Path "requirements.txt") {
    Write-Host "Instalando dependências..."
    pip install -r requirements.txt
} else {
    Write-Host "requirements.txt não encontrado."
}

Write-Host "Setup finalizado com sucesso!"

# --- Estágio de Build ---
# Usa uma imagem Python completa para instalar dependências
FROM python:3.11-slim as builder

# Define o diretório de trabalho
WORKDIR /app

# Instala o Poetry
RUN pip install poetry

# Copia os arquivos de definição de dependências
COPY pyproject.toml poetry.lock ./

# Instala as dependências de produção, ignorando as de desenvolvimento
RUN poetry install --no-dev --no-interaction --no-ansi

# --- Estágio Final ---
# Usa uma imagem Python slim para a aplicação final
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o ambiente virtual com as dependências do estágio de build
COPY --from=builder /app/.venv /.venv

# Define o PATH para que os executáveis do .venv sejam encontrados
ENV PATH="/app/.venv/bin:$PATH"

# Copia o código da aplicação
COPY app/ ./app

# Expõe a porta que a aplicação vai rodar
EXPOSE 8000

# Comando para iniciar a aplicação com Uvicorn
# --host 0.0.0.0 é crucial para que a aplicação seja acessível de fora do container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

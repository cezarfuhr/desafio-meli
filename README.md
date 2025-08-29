# Desafio Meli - API de Detalhes do Item

API desenvolvida como parte do desafio técnico de backend do Mercado Livre.

Este projeto cria uma API containerizada para servir detalhes de produtos, seguindo as melhores práticas de arquitetura de software, testes e automação.

**Stack Tecnológica:**
*   Python 3.11+
*   FastAPI
*   Poetry
*   Pytest
*   Docker & Docker Compose

## Como Executar

Este projeto é totalmente containerizado. O único pré-requisito é ter **Docker** e **Docker Compose** instalados.

Para instruções detalhadas de como construir a imagem, iniciar a aplicação, parar a aplicação e rodar os testes, por favor, consulte o documento:

➡️ **[./run.md](./run.md)**

## Estrutura do Projeto (Saga 01)

A arquitetura do projeto ao final da Saga 01 estabelece a fundação para o desenvolvimento:

-   `app/main.py`: Ponto de entrada da aplicação FastAPI e endpoint "Hello World".
-   `tests/test_api.py`: Teste de integração para o endpoint "Hello World".
-   `Dockerfile`: Receita para construir a imagem da aplicação.
-   `docker-compose.yml`: Orquestra a execução do container.
-   `pyproject.toml` / `poetry.lock`: Gerenciamento de dependências.
-   `docs/sagas/`: Documentação incremental da arquitetura e decisões de projeto.

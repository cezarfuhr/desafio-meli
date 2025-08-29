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

## Estratégia de Logging e Observabilidade

Este projeto implementa uma estratégia de logging estruturado que facilita a integração com qualquer plataforma de observabilidade moderna.

### Abordagem de Logging

**Formato Estruturado JSON:** Todos os logs são emitidos em formato JSON estruturado para `stdout`, facilitando:
- Parsing automático por sistemas de agregação de logs
- Filtragem e busca eficientes por campos específicos  
- Integração nativa com stacks como ELK, Splunk, Datadog, etc.

**Exemplo de saída de log:**
```json
{
  "timestamp": "2024-01-15T10:30:45.123456",
  "level": "INFO",
  "name": "app.services.item_service",
  "message": "Item found: iPhone 14 Pro Max (ID: MLB123456789)",
  "module": "item_service",
  "function": "get_item_by_id",
  "line": 56
}
```

### Integração com Plataformas de Observabilidade

O padrão de logging para `stdout` permite integração transparente com qualquer sistema:

**Exemplo - Papertrail via Syslog Driver:**
```yaml
# docker-compose.yml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    logging:
      driver: syslog
      options:
        syslog-address: "tcp://logs.papertrailapp.com:XXXXX"
        tag: "desafio-meli-api"
```

**Outras integrações suportadas:**
- AWS CloudWatch Logs (driver `awslogs`)
- Google Cloud Logging (driver `gcplogs`) 
- Fluentd (driver `fluentd`)
- Splunk (driver `splunk`)

## Estrutura do Projeto

### Saga 01 - Fundação
A arquitetura do projeto estabelece a fundação para o desenvolvimento:

-   `app/main.py`: Ponto de entrada da aplicação FastAPI e endpoint "Hello World".
-   `tests/test_api.py`: Teste de integração para o endpoint "Hello World".
-   `Dockerfile`: Receita para construir a imagem da aplicação.
-   `docker-compose.yml`: Orquestra a execução do container.
-   `pyproject.toml` / `poetry.lock`: Gerenciamento de dependências.
-   `docs/sagas/`: Documentação incremental da arquitetura e decisões de projeto.

### Saga 02 - O Item
Implementação da lógica de negócio com arquitetura limpa:

-   `app/models/item.py`: Modelo Pydantic para representação de itens
-   `app/repository/item_repository.py`: Camada de acesso a dados
-   `app/services/item_service.py`: Lógica de negócio e exceções customizadas
-   `app/api/v1/items.py`: Endpoints REST com injeção de dependência
-   `app/core/logging_config.py`: Configuração centralizada de logging estruturado
-   `data/items.json`: Base de dados simulada para desenvolvimento

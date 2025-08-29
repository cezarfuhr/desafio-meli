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

## Decisões Arquitetônicas Chave

Este projeto foi construído com várias decisões de arquitetura intencionais para garantir robustez, manutenibilidade e alinhamento com as práticas modernas de engenharia de software:

1.  **Arquitetura em Camadas (Ports and Adapters):** A aplicação é dividida em camadas distintas (API, Serviços, Repositório) para separar as responsabilidades. Isso garante que a lógica de negócio (`services`) não dependa de detalhes de implementação, como o framework web (`api`) ou o método de persistência (`repository`).

2.  **Containerização com Docker:** Todo o ambiente de desenvolvimento e produção é containerizado. Isso resolve o problema de "funciona na minha máquina", garante consistência entre ambientes e simplifica drasticamente a execução do projeto para qualquer pessoa. O `Dockerfile` multi-stage cria uma imagem final otimizada, contendo apenas o necessário para a execução.

3.  **Logging Estruturado para `stdout`:** Seguindo a metodologia "Twelve-Factor App", a aplicação não escreve logs em arquivos. Em vez disso, emite logs estruturados (JSON) para a saída padrão, delegando a responsabilidade de coleta e armazenamento para o ambiente de execução (Docker). Isso torna a aplicação agnóstica em relação à plataforma de observabilidade e pronta para integração com sistemas de monitoramento de nível empresarial.

4.  **Gerenciamento de Dependências com Poetry:** Usamos Poetry e seu arquivo `poetry.lock` para garantir builds 100% reprodutíveis. Qualquer pessoa que construir o projeto terá o mesmo conjunto exato de dependências, eliminando conflitos de versão.

## Estratégia Técnica e Uso de IA

A eficiência do desenvolvimento foi aprimorada através de uma combinação de ferramentas modernas e um fluxo de trabalho assistido por IA.

-   **Stack Tecnológica:** A escolha por **Python/FastAPI** foi deliberada para maximizar a velocidade de desenvolvimento, aproveitar a validação de dados nativa com Pydantic e obter documentação de API (Swagger UI) automaticamente.
-   **Fluxo de Trabalho Arquiteto/Implementador:** Utilizamos um modelo de colaboração onde uma IA (Gemini) atua como o **Arquiteto de Software**, responsável pelo planejamento, design, documentação e revisão. Outra IA (Claude) atua como o **Implementador**, focada em traduzir os blueprints do arquiteto em código limpo e funcional. Este processo, documentado em `prompts.md`, permitiu uma separação clara de responsabilidades e acelerou o ciclo de desenvolvimento.

### Saga 02 - O Item
Implementação da lógica de negócio com arquitetura limpa:

-   `app/models/item.py`: Modelo Pydantic para representação de itens
-   `app/repository/item_repository.py`: Camada de acesso a dados
-   `app/services/item_service.py`: Lógica de negócio e exceções customizadas
-   `app/api/v1/items.py`: Endpoints REST com injeção de dependência
-   `app/core/logging_config.py`: Configuração centralizada de logging estruturado
-   `data/items.json`: Base de dados simulada para desenvolvimento

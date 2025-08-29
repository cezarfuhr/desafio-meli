### **Plano de Execução Detalhado: Saga 01 - A Fundação (Revisão Final)**

**Objetivo:** Criar, testar e documentar um projeto "Hello World" em FastAPI, gerenciado por Poetry e containerizado com Docker/Docker Compose, com um workflow Git estabelecido.

**Metadados do Projeto:**
*   **Nome do Pacote:** `desafio_meli`
*   **Versão:** `0.1.0`
*   **Descrição:** `API para o desafio de backend do Mercado Livre.`
*   **Autor:** `Cezar Fuhr <cezar@nextar.com.br>`
*   **Licença:** `MIT`
*   **Versão do Python:** `^3.11`

---

### **Passos de Implementação**

**1. Estrutura de Diretórios Inicial:**
   - [X] Criar os diretórios `app`, `docs/sagas`, e `tests`.

**2. Formalizar a Saga 01 em um Documento:**
   - [X] Criar este arquivo `docs/sagas/01_fundacao.md`.

**3. Inicialização do Projeto Python com Poetry:**
   - [ ] Inicializar o projeto Poetry com os metadados definidos.
   - [ ] Configurar o Poetry para criar o `.venv` dentro do projeto.
   - [ ] Adicionar dependências de produção: `fastapi`, `uvicorn[standard]`.
   - [ ] Adicionar dependências de desenvolvimento: `pytest`, `httpx`.

**4. Esqueleto da Aplicação "Hello World":**
   - [ ] Criar o arquivo `app/main.py` com um endpoint GET `/` que retorna `{"message": "..."}`.

**5. Containerização com Docker:**
   - [ ] Criar os arquivos `.gitignore` e `.dockerignore`.
   - [ ] Criar um `Dockerfile` multi-stage para construir uma imagem de produção otimizada.
   - [ ] Criar um `docker-compose.yml` para orquestrar a execução do container.

**6. Testes e Automação:**
   - [ ] Criar `tests/test_api.py` para validar o endpoint `/`.
   - [ ] Criar um script `run.sh` para simplificar a execução (`docker-compose up --build`).
   - [ ] Tornar o script `run.sh` executável.

**7. Documentação e Versionamento:**
   - [ ] Criar um `README.md` inicial.
   - [ ] Criar o arquivo `run.md` com as instruções de execução.
   - [ ] Inicializar o repositório Git e realizar o primeiro commit.

---
**Critério de Sucesso para esta Saga:**
O comando `./run.sh` deve subir um container, e ao acessar `http://localhost:8000` no navegador, a mensagem de "Hello World" da API deverá ser exibida. O comando `pytest` deve executar com sucesso.

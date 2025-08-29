### **Plano de Arquitetura: Adendo à Saga 02 (Saga 2.1) - Aprimoramento da Observabilidade**

**Objetivo:**
Elevar a maturidade do nosso sistema de logging, passando de um formato de texto simples para um formato estruturado (JSON), e documentar formalmente nossa estratégia de observabilidade.

**Estado Inicial:**
A implementação da Saga 02, com logging básico para `stdout`.

**Estado Final Desejado:**
*   Todos os logs emitidos pela aplicação estarão no formato JSON.
*   O `README.md` conterá uma seção detalhada explicando nossa estratégia de logging e como ela permite a integração com qualquer plataforma de observabilidade.

---

### **Passos de Implementação (Blueprint para o Implementador):**

**1. Implementar o `JSONFormatter`:**
   - [ ] No arquivo `app/core/logging_config.py`, criar uma nova classe `JSONFormatter` que herda de `logging.Formatter`.
   - [ ] O método `format(self, record)` desta classe deve construir um dicionário Python com os atributos de log desejados (ex: `timestamp`, `level`, `name`, `message`) e convertê-lo para uma string JSON.
   - [ ] Modificar a função `configure_logging` para usar este novo `JSONFormatter` em vez do formatador de texto.

**2. Atualizar a Documentação:**
   - [ ] No arquivo `README.md`, adicionar a seção "Estratégia de Logging e Observabilidade" que discutimos. O texto deve explicar a abordagem de `stdout` e dar o exemplo de configuração do `docker-compose.yml` para um `syslog driver` como o Papertrail.

**3. Testar a Nova Configuração:**
   - [ ] Reiniciar a aplicação com `./run.sh`.
   - [ ] Visualizar os logs com `docker compose logs api`.
   - [ ] **Critério de Sucesso:** A saída dos logs deve estar em formato JSON.

**4. Registrar o Marco (Commit):**
   - [ ] Ao final de todos os passos, fazer um commit com uma mensagem clara.
   - [ ] **Sugestão de Mensagem:** `feat(logging): implement structured JSON logging`

---

**Observação para o Implementador:**
A mudança deve ser contida apenas em `app/core/logging_config.py`. Nenhuma outra parte do código que usa o logger (`app/main.py`, `app/services/...`) precisará ser alterada. Esta é a beleza de uma configuração centralizada.

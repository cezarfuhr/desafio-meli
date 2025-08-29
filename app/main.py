from fastapi import FastAPI

app = FastAPI(title="Desafio Meli API")


@app.get("/", tags=["Health Check"])
def read_root():
    """
    Endpoint raiz para verificar a saúde da aplicação.
    """
    return {"message": "Hello, Architect! The foundation is solid."}

from fastapi import FastAPI

app = FastAPI(
    title="Pokemon API",
    description="Projeto para batalhas de pokemons",
    version="0.1.0"
)


@app.get("/mensagem")
def mensagem():
    """Rota para uma mensagem de boas vindas"""
    return {"mensagem": "Olá mundo"}

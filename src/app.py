from fastapi import FastAPI
from pathlib import Path
from controllers import calculadora_controller
import sys

# Permite rodar com `py src/app.py`: coloca a raiz do projeto no sys.path
# Para os imports `from src import .` funcionarem corretamente

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

app = FastAPI(
    title="Pokemon API",
    description="Projeto para batalhas de pokemons",
    version="0.1.0"
)


app.include_router(calculadora_controller.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)
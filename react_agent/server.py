from fastapi import FastAPI
import sys
import os
from langserve import add_routes

# Aseguramos que ReactAgent (raíz) esté en sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importamos el graph compilado
from graph import graph

app = FastAPI(
    title="Socrates Assistant API",
    version="0.1",
    description="API para interactuar con el agente Socrates impulsado por Langgraph",
)

# Agrega las rutas de Langserve al grafo
add_routes(app, graph, path="/socrates")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

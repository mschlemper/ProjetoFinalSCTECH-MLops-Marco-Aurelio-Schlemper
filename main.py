from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.services import carregar_modelo, limpar_modelo
from app.routers import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicialização da aplicação (Fase 3)
    carregar_modelo()
    yield
    # Encerramento da aplicação
    limpar_modelo()

app = FastAPI(
    title="API de Análise Preditiva de Risco de Crédito",
    description="Microsserviço de Machine Learning para predição de risco financeiro.",
    version="1.0.0",
    lifespan=lifespan
)

# Inclui as rotas expostas pelo roteador
app.include_router(router)

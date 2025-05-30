from fastapi import FastAPI
from backend.api.routes import router as api_router

app = FastAPI(title="Dashboard Analítico")

app.include_router(api_router)

# Criação automática da tabela no SQLite
from backend.models.base import Base, engine
import backend.models.etl_data  # garante que o modelo é importado

Base.metadata.create_all(bind=engine)

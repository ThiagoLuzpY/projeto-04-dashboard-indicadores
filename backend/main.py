from fastapi import FastAPI
from backend.api.routes import router as api_router

app = FastAPI(title="Dashboard Analítico")
app.include_router(api_router)

# Criação automática da tabela no SQLite
import os
from backend.models.base import Base, engine
import backend.models.etl_data  # garante que o modelo é importado

# 🚀 Se não existir o banco de dados, cria automaticamente
db_path = "/app/backend/data.db"
if not os.path.exists(db_path):
    print("💾 data.db não encontrado... criando automaticamente as tabelas.")
    Base.metadata.create_all(bind=engine)
else:
    print("💾 Banco já existe, não é necessário criar tabelas.")

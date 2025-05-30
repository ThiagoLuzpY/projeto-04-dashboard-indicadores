from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from backend.etl.etl_pipeline import run_etl_pipeline
from backend.auth.users import authenticate_user
from backend.auth.security import (
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    decode_access_token,
    get_current_user
)
from backend.models.base import SessionLocal
from backend.models.etl_data import EtlData

from datetime import timedelta
from typing import List
import shutil
from pathlib import Path
import pandas as pd
import chardet

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Dashboard Analítico - API Online"}


@router.post("/upload-etl")
async def upload_etl(
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user)
):
    try:
        temp_dir = Path("temp_uploads")
        temp_dir.mkdir(exist_ok=True)
        temp_file = temp_dir / file.filename

        with open(temp_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        with open(temp_file, "rb") as f:
            result = chardet.detect(f.read())
            encoding = result["encoding"]

        run_etl_pipeline(str(temp_file))

        df = pd.read_csv(temp_file, sep=";", encoding=encoding)
        rows, cols = df.shape

        return {
            "status": "success",
            "rows_loaded": rows,
            "columns_loaded": cols,
            "encoding_used": encoding
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro interno ao processar ETL: {str(e)}"
        )


@router.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/etl-data")
async def get_etl_data(limit: int = 100):
    try:
        db = SessionLocal()
        records = db.query(EtlData).limit(limit).all()
        return [
            {
                "id": r.id,
                "uf": r.uf,
                "vendedor": r.vendedor
            }
            for r in records
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar dados: {str(e)}")
    finally:
        db.close()



from backend.models.kpi import calcular_kpis
from backend.models.base import SessionLocal

@router.get("/kpi")
async def get_kpis():
    try:
        db = SessionLocal()
        result = calcular_kpis(db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao calcular KPIs: {str(e)}")
    finally:
        db.close()


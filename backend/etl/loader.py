from backend.models.etl_data import EtlData
from backend.models.base import SessionLocal
import pandas as pd

def persist_to_db(df: pd.DataFrame):
    session = SessionLocal()
    try:
        for _, row in df.iterrows():
            record = EtlData(
                uf=row.get("uf") or "N/A",
                vendedor=row.get("vendedor") or "N/A"
            )
            session.add(record)
        session.commit()
        print("✅ Dados persistidos com sucesso")
    except Exception as e:
        session.rollback()
        print(f"🔥 Erro ao persistir no banco: {e}")
        raise
    finally:
        session.close()

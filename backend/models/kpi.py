from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.models.etl_data import EtlData

def calcular_kpis(db: Session):
    # 📍 Total de clientes por UF
    clientes_por_uf = (
        db.query(EtlData.uf, func.count(EtlData.id).label("qtd_clientes"))
        .group_by(EtlData.uf)
        .all()
    )

    # 📍 Total de clientes por Vendedor
    clientes_por_vendedor = (
        db.query(EtlData.vendedor, func.count(EtlData.id).label("qtd_clientes"))
        .group_by(EtlData.vendedor)
        .all()
    )

    return {
        "clientes_por_uf": [
            {"uf": uf, "qtd": qtd} for uf, qtd in clientes_por_uf
        ],
        "clientes_por_vendedor": [
            {"vendedor": vendedor, "qtd": qtd} for vendedor, qtd in clientes_por_vendedor
        ]
    }

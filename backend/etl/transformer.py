import pandas as pd
from typing import Dict

def clean_data(df: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
    print("🔍 Colunas antes do renomeio:")
    print(df.columns.tolist())

    # Renomear colunas conforme mapeamento
    df = df.rename(columns=mapping)

    print("✅ Colunas após o mapeamento:")
    print(df.columns.tolist())

    # Verificação de colunas obrigatórias
    cols_necessarias = ["uf", "vendedor"]
    for col in cols_necessarias:
        if col not in df.columns:
            raise Exception(f"❌ Coluna obrigatória ausente após mapeamento: {col}")

    # Limpeza de nulos
    df["uf"] = df["uf"].fillna("N/A")
    df["vendedor"] = df["vendedor"].fillna("N/A")

    return df

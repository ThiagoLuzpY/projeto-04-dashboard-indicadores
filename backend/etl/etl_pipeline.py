from backend.etl.extractor import extract_data
from backend.etl.transformer import clean_data
from backend.etl.loader import persist_to_db

# 🔁 Novo mapeamento: CSV → modelo
mapping = {
    "UF": "uf",
    "Vendedor": "vendedor"
}


def run_etl_pipeline(csv_path: str):
    """Executa o pipeline ETL completo com mapeamento de UF e Vendedor."""

    print(f"➡️ Iniciando extração de {csv_path}...")
    df = extract_data(csv_path)
    print(f"✅ Dados extraídos: {df.shape[0]} linhas e {df.shape[1]} colunas.")

    df_cleaned = clean_data(df, mapping)
    print(f"✅ Dados transformados: {df_cleaned.shape[0]} linhas e {df_cleaned.shape[1]} colunas.")

    persist_to_db(df_cleaned)
    print("✅ Dados persistidos no banco com sucesso!")

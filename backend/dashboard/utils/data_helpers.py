import pandas as pd


def filter_dataframe(df: pd.DataFrame, uf_col="uf", vendedor_col="vendedor") -> pd.DataFrame:
    """
    Renderiza dois filtros (UF e Vendedor) no Streamlit e retorna o DataFrame filtrado.
    """
    import streamlit as st  # Import local: protege contra falhas fora do Streamlit

    df_filtered = df.copy()

    # Colunas normalizadas
    df_filtered = normalize_column_names(df_filtered)

    # Validar existência antes de filtrar
    ufs = sorted(df_filtered[uf_col].dropna().unique()) if uf_col in df_filtered else []
    vendedores = sorted(df_filtered[vendedor_col].dropna().unique()) if vendedor_col in df_filtered else []

    col1, col2 = st.columns(2)
    uf_selected = col1.selectbox("Filtrar por UF", options=["Todos"] + ufs)
    vend_selected = col2.selectbox("Filtrar por Vendedor", options=["Todos"] + vendedores)

    if uf_selected != "Todos" and uf_col in df_filtered:
        df_filtered = df_filtered[df_filtered[uf_col] == uf_selected]
    if vend_selected != "Todos" and vendedor_col in df_filtered:
        df_filtered = df_filtered[df_filtered[vendedor_col] == vend_selected]

    return df_filtered


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Deixa os nomes de colunas lowercase e sem espaços/hífens para consistência.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df

import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import os
from core_services import fetch_kpis, fetch_etl_data


# ⬇️ Imports relativos corrigidos
from utils.data_helpers import filter_dataframe
from utils.style_config import inject_custom_css

import os

API_URL = os.getenv("API_URL")
if not API_URL:
    API_URL = "http://127.0.0.1:8000"
API_URL = API_URL.rstrip("/")

# ⚙️ Config inicial
st.set_page_config(page_title="Dashboard Analítico", layout="wide")
inject_custom_css()

# 🔐 Login interativo
if "token" not in st.session_state:
    st.title("🔐 Login necessário para acessar o Dashboard")
    with st.form("login_form"):
        username = st.text_input("Usuário", value="admin")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            url = f"{API_URL}/auth/login"
            data = {"username": username, "password": password}
            response = requests.post(url, data=data)
            if response.status_code == 200:
                token = response.json()["access_token"]
                st.session_state["token"] = token
                st.rerun()
            else:
                st.error("❌ Falha no login.")
    st.stop()

# ✅ Se logado, carrega o dashboard normal
st.title("📊 Dashboard Analítico de Clientes")
token = st.session_state["token"]
headers = {"Authorization": f"Bearer {token}"}

# 🔁 Carregar KPIs e Dados
with st.spinner("🔄 Carregando dados da API..."):
    try:
        kpi_data = requests.get(f"{API_URL}/kpi", headers=headers).json()
        df = requests.get(f"{API_URL}/etl-data?limit=2000", headers=headers).json()
        df = pd.DataFrame(df)
    except Exception as e:
        st.error(f"❌ Erro ao buscar dados: {e}")
        st.stop()

# 📌 Mostrar KPI Geral
st.subheader("📌 KPIs por UF e por Vendedor")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👥 Clientes por UF")
    df_uf = pd.DataFrame(kpi_data["clientes_por_uf"])
    fig_uf = px.bar(df_uf.sort_values("qtd", ascending=False), x="uf", y="qtd",
                    labels={"uf": "Estado", "qtd": "Qtd. de Clientes"},
                    title="Distribuição por Estado (UF)")
    st.plotly_chart(fig_uf, use_container_width=True)

with col2:
    st.markdown("### 💼 Clientes por Vendedor")
    df_vend = pd.DataFrame(kpi_data["clientes_por_vendedor"])
    fig_vend = px.bar(df_vend.sort_values("qtd", ascending=False).head(20),
                      x="qtd", y="vendedor", orientation="h",
                      labels={"vendedor": "Vendedor", "qtd": "Clientes"},
                      title="Top 20 Vendedores por Número de Clientes")
    st.plotly_chart(fig_vend, use_container_width=True)

# 📄 Exibir tabela com filtros
st.subheader("📄 Visualização de Dados Brutos")

if not df.empty:
    filtered_df = filter_dataframe(df, uf_col="categoria", vendedor_col="fornecedor")
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.warning("Nenhum dado encontrado.")

# 📊 Dashboard Analítico de Clientes — Projeto ETL, API e Dashboard

Este projeto é um sistema completo para **análise de indicadores** a partir de dados carregados via arquivos CSV, com um **pipeline ETL**, **API RESTful protegida** por JWT e um **dashboard interativo** em Streamlit. Tudo modularizado e pronto para produção! 🚀

---

## 💡 Visão Geral

✅ **Pipeline ETL** para leitura, limpeza e persistência de dados.  
✅ **API (FastAPI)** com autenticação JWT e endpoints protegidos.  
✅ **Dashboard (Streamlit)** para visualização interativa dos dados.  
✅ **Banco de Dados SQLite** para armazenamento persistente.  
✅ **Docker Compose** para orquestração e deploy local/produção.  
✅ **Testes automatizados (pytest)** garantindo a qualidade do código.

---

## 🗂️ Estrutura de Pastas

projeto-04-dashboard-indicadores/
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── security.py
│   │   └── users.py
│   │
│   ├── dashboard/
│   │   ├── __init__.py
│   │   ├── app_dashboard.py
│   │   ├── core_services.py
│   │   ├── data_helpers.py
│   │   ├── style_config.py
│   │   └── Dockerfile.dashboard
│   │
│   ├── etl/
│   │   ├── __init__.py
│   │   ├── etl_pipeline.py
│   │   ├── extractor.py
│   │   ├── loader.py
│   │   └── transformer.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── etl_data.py
│   │   ├── forecast.py
│   │   ├── kpi.py
│   │   ├── main.py
│   │   └── Dockerfile.backend
│   │
│   └── main.py
│
├── temp_uploads/           # Pasta para arquivos CSV temporários
│
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_etl.py
│   ├── test_models.py
│   └── test_etl_script.py
│
├── data.db                 # Banco SQLite local
├── docker-compose.yml
├── Dockerfile              # (opcional) Dockerfile base para personalização
├── README.md
├── requirements.txt
└── .gitignore




---

## ⚙️ Tecnologias e Ferramentas

- **🐍 Python 3.11**  
- **FastAPI** — API RESTful moderna e performática  
- **SQLAlchemy** — ORM para persistência em SQLite  
- **Streamlit** — Dashboard interativo e rápido de implementar  
- **pandas** — Manipulação de dados tabulares  
- **Plotly** — Gráficos dinâmicos e responsivos  
- **requests** — Consumo de APIs no dashboard  
- **pytest** — Testes automatizados  
- **bcrypt** — Criptografia de senhas (usuários fictícios)  
- **Docker Compose** — Orquestração de múltiplos serviços (backend + dashboard)  
- **Docker** — Contêinerização para ambientes reproduzíveis  
- **WSL2 / Linux** — Melhor performance para desenvolvimento (no Windows, via Docker Desktop)  

---

## 🚀 Como Executar Localmente (sem Docker)

1️⃣ Ative seu ambiente virtual:  
```bash
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows


2️⃣ Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt


3️⃣ Rode o backend (FastAPI):

bash
Copiar
Editar
uvicorn backend.main:app --reload


4️⃣ Rode o dashboard (Streamlit):

streamlit run backend/dashboard/app_dashboard.py

Acesse:

API Docs: http://127.0.0.1:8000/docs

Dashboard: http://localhost:8501


🐳 Como Executar com Docker Compose

docker compose up --build


Pronto! O Compose vai subir dois serviços:

🟦 backend na porta 8000

🟧 dashboard na porta 8501

🔒 Autenticação
Usuários fictícios estão em backend/auth/users.py.

Use credenciais como:

Usuário: admin

Senha: admin123

🔍 Funcionalidades
✅ Upload seguro de CSV pela API (/upload).
✅ Pipeline ETL automático:

extractor.py: leitura e encoding automático

transformer.py: limpeza e padronização

loader.py: persistência via ORM
✅ Endpoints de consulta (/etl-data, /kpi).
✅ Dashboard:

Gráficos de clientes por UF e por vendedor.

Tabela de dados brutos com filtros dinâmicos.
✅ Testes automatizados (tests/).

📈 Extensibilidade
Forecast futuro: arquivo forecast.py para predições.

KPIs adicionais: prontos para expansão em models/kpi.py.

Banco de produção: fácil migração para PostgreSQL, MySQL, etc.

🛡️ Observações Finais
O .env não foi usado, mas variáveis de ambiente são injetadas via docker-compose.yml diretamente.

Ideal para:

🏢 Pequenas empresas que usam Excel e querem automação

📊 Cientistas de dados que precisam de um pipeline ETL + dashboard rápido

⚡ Desenvolvedores que queiram exemplos reais de integração entre FastAPI e Streamlit

👤 Autor e Contato
🚀 Feito por Thiago, com consultoria de 🥷 Jake (AI coding ninja)
📧 [Seu e-mail ou LinkedIn]
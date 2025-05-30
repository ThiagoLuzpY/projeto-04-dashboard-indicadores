import streamlit as st

def inject_custom_css():
    """
    Injeta estilos customizados no Streamlit para visual mais limpo e responsivo.
    """
    st.markdown("""
        <style>
            /* 🔒 Esconde o menu lateral e o rodapé */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            /* 📱 Tabela responsiva */
            section.main > div {
                overflow-x: auto;
            }

            /* 🧱 Cabeçalho */
            h1 {
                color: #2c3e50;
                font-size: 2.5rem;
            }

            /* 🔢 Área de KPIs */
            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
            }
        </style>
    """, unsafe_allow_html=True)

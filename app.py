import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu Portfólio de Dados", page_icon="💼", layout="wide")

# Cabeçalho / Perfil
st.title("João Silva")
st.subheader("Engenheiro de Dados & Especialista em BI")
st.write("📍 São Paulo, Brasil | [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)")

st.divider()

# Divisão em colunas para organizar o conteúdo
col1, col2 = st.columns([1, 2])

with col1:
    st.header("🛠️ Habilidades")
    st.markdown("- **Linguagens:** Python, SQL")
    st.markdown("- **BI:** Power BI, Looker, Tableau")
    st.markdown("- **Engenharia:** Apache Airflow, BigQuery, dbt")

with col2:
    st.header("🚀 Projetos em Destaque")
    
    # Projeto 1
    with st.expander("Pipeline de Dados com Airflow & BigQuery"):
        st.write("Orquestração de dados brutos de uma API até o data warehouse.")
        st.markdown("[Ver código no GitHub](https://github.com)")
        
    # Projeto 2
    with st.expander("Dashboard de Performance de Vendas"):
        st.write("Painel interativo focado no acompanhamento de KPIs de receita.")
        st.markdown("[Ver projeto interativo](https://novypro.com)")

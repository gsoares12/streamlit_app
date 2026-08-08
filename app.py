import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu Portfólio de Dados", page_icon="💼", layout="wide")

# Cabeçalho / Perfil
st.title("Guilherme Soares")
st.subheader("Engenheiro de Dados")
st.write("Belo Horizonte, Brasil | [LinkedIn](www.linkedin.com/in/guilherme-henrique-soares-343481197) | [GitHub](https://github.com/gsoares12)")

st.divider()

# Divisão em colunas para organizar o conteúdo
col1, col2 = st.columns([1, 2])

with col1:
    st.header("🛠️ Habilidades")
    st.markdown("- **Linguagens:** Python, SQL, APIs, Bash, PowerShell, HTML, CSS")
    st.markdown("- **BI:** Power BI,")
    st.markdown("- **Engenharia:** Apache Airflow, BigQuery, Docker, Git, CI/CD, ")

with col2:
    st.header("🚀 Projetos em Destaque")
    
    # Projeto 1
    with st.expander("Pipeline de Dados com Airflow & BigQuery"):
        st.write("Orquestração de dados brutos de uma API até o data warehouse.")
        st.markdown("[Ver código no GitHub](https://github.com)")
        
    # Projeto 2
    with st.expander("Dashboard de Alarmes gerados por sensores IoT"):
        st.write("Painel interativo focado no acompanhamento de KPIs de alarmes gerados em sensores IoT.")
        
        # Inserindo a imagem local do seu projeto
        st.image(r".\img\exemplo_01.png", caption="Pré-visualização do Dashboard de Alarmes", use_container_width=True)
        
        # st.markdown("[Ver projeto interativo](https://novypro.com)")
     
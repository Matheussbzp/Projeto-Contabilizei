import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("Carreira de Cientista de Dados")

    # Sidebar
    st.sidebar.title("Detalhes de Carreira")

    # Bloco "Cientista de Dados"
    st.sidebar.header("Cientista de Dados")

    # Subtítulos
    st.sidebar.subheader("Tributações")
    st.sidebar.info("CLT: 15%")
    st.sidebar.info("PJ: 75% (25% INSS + 50% IR)")

    st.sidebar.subheader("Trilha de Carreira")
    st.sidebar.write("**Recursos:**")
    st.sidebar.write("- Sugestões de cursos e treinamentos para aprimorar suas habilidades.")
    st.sidebar.write("- Comparação da carreira de Cientista de Dados com outras áreas (Engenheiro de Software, Analista de Cibersegurança).")

    st.sidebar.subheader("Guia do Autônomo")
    st.sidebar.write("**Informações:**")
    st.sidebar.write("- Como se tornar um profissional autônomo.")
    st.sidebar.write("- Dicas para encontrar clientes e gerenciar seu negócio.")

    st.sidebar.subheader("Guia PJ x CLT")
    st.sidebar.write("**Comparação:**")
    st.sidebar.write("- Vantagens e desvantagens de cada regime de trabalho.")

    # Bloco "Empresas"
    st.header("Empresas")
    st.write("- XPTO Inc.")
    st.write("- SoftBank")

    # Bloco central com informações
    st.header("Informações Gerais")

    # Média salarial
    st.subheader("Média Salarial")
    st.info("R$ 6.500,00")

    # Tributação
    st.subheader("Tributação")
    st.info("CLT: 15%")
    st.info("PJ: 75%")

    # Comparativo PJ x CLT
    st.subheader("Comparativo PJ x CLT")
    fig_pj_clt, ax_pj_clt = plt.subplots(figsize=(8, 5))
    clt_pj_labels = ["CLT", "PJ"]
    clt_pj_values = [6000, 15000]  # Valores fictícios
    ax_pj_clt.barh(clt_pj_labels, clt_pj_values, color=['#85B6FF', '#FFFBFB'])
    ax_pj_clt.set_xlabel("Salário (R$)")
    ax_pj_clt.set_title("Salário CLT x PJ")
    ax_pj_clt.grid(axis='x', linestyle='--', alpha=0.7)
    ax_pj_clt.spines['top'].set_visible(False)
    ax_pj_clt.spines['right'].set_visible(False)

    # Adicionar rótulos aos pontos
    for i, salario in enumerate(clt_pj_values):
        ax_pj_clt.text(salario, i, f"{salario} R$", va='center', ha='left')

    st.pyplot(fig_pj_clt)

    # Média de Salário por Estado
    st.subheader("Média de Salário por Estado")
    st.write("**Estado com maior salário:** São Paulo")
    st.write("**Estado com menor salário:** Rio Grande do Sul")

    # Gráfico de Salário por Estado
    fig_salario_estado, ax_salario_estado = plt.subplots(figsize=(10, 6))
    estados = ["SP", "RJ", "MG", "RS"]
    salarios = [8500, 7800, 7200, 6900]  # Média salarial fictícia
    ax_salario_estado.bar(estados, salarios, color='#0EF4F7')
    ax_salario_estado.set_xlabel("Estado")
    ax_salario_estado.set_ylabel("Média Salarial")
    ax_salario_estado.set_title("Média de Salário por Estado")
    ax_salario_estado.grid(axis='y', linestyle='--', alpha=0.7)
    ax_salario_estado.spines['top'].set_visible(False)
    ax_salario_estado.spines['right'].set_visible(False)

    # Adicionar rótulos aos pontos
    for i, salario in enumerate(salarios):
        ax_salario_estado.text(estados[i], salario, f"{salario} R$", ha='center', va='bottom')

    st.pyplot(fig_salario_estado)

    # Compare com outras carreiras
    st.subheader("Compare com outras carreiras:")
    st.write("- Engenheiro de Software")
    st.write("- Analista de TI")
    st.write("- Analista de Cibersegurança")
    st.write("- Engenheiro de Dados")

    # Competências e Requisitos
    st.header("Competências e Requisitos")
    st.write("- Python")
    st.write("- SQL")
    st.write("- PowerBI")

    # Dados do mercado
    crescimento_mercado = [
        100, 120, 180, 250
    ]

    # Anos
    anos = [2020, 2021, 2022, 2023]

    # Plotar o gráfico de crescimento do mercado
    fig_crescimento_mercado, ax_crescimento_mercado = plt.subplots(figsize=(10, 8))
    ax_crescimento_mercado.plot(anos, crescimento_mercado, marker='o', color='blue', linewidth=2)
    ax_crescimento_mercado.set_xlabel("Ano")
    ax_crescimento_mercado.set_ylabel("Crescimento do Mercado (em milhões)")
    ax_crescimento_mercado.set_title("Crescimento do Mercado (2020 - 2023)")
    ax_crescimento_mercado.grid(axis='y', linestyle='--', alpha=0.7)
    ax_crescimento_mercado.spines['top'].set_visible(False)
    ax_crescimento_mercado.spines['right'].set_visible(False)

    # Adicionar marcadores de semestre
    anos_semestres = [f"{ano}" for ano in anos]
    ax_crescimento_mercado.set_xticks(anos)
    ax_crescimento_mercado.set_xticklabels(anos_semestres, rotation=45, ha='right')

    # Adicionar rótulos aos pontos
    for i, crescimento in enumerate(crescimento_mercado):
        ax_crescimento_mercado.text(anos[i], crescimento, f"{crescimento}M", ha='center', va='bottom')

    st.pyplot(fig_crescimento_mercado)

if __name__ == "__main__":
    main()
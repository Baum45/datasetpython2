import pandas as pd 
import streamlit as st  
import plotly.express as px
from utils.carrega_dados import carregar_dados,remove_outliers_iqr

df = carregar_dados()   

st.subheader("📦 Apresento o Boxplot da Distribuição de Notas por Fatores Familiares")
st.write("Utilize os filtros para ajustar o gráfico conforme desejado.")

col1, col2, col3 = st.columns(3)

with col1:
    Envolvimento_Parental = st.multiselect(
        "Envolvimento dos Pais",
        options=df['Envolvimento_Parental'].unique(),
        default=df['Envolvimento_Parental'].unique(),
        key="parental_involvement_1"  #key chave unica para nao da conflito com os outros multiselects... obs: estava com esse problema
    )

with col2:
    Renda_Familiar = st.multiselect(
        "Renda Familiar",
        options=df['Renda_Familiar'].unique(),
        default=df['Renda_Familiar'].unique(),
        key="family_income_1"  
    )

with col3:
    parental_education = st.multiselect(
        "Escolaridade dos Pais",
        options=df['Nivel_de_Educacao_Parental'].unique(),
        default=df['Nivel_de_Educacao_Parental'].unique(),
        key="parental_education_1"  
    )

show_outliers = st.toggle("Mostrar Outliers", value=False, key="show_outliers_1")

filtered_df = df[
    (df['Envolvimento_Parental'].isin(Envolvimento_Parental)) &
    (df['Renda_Familiar'].isin(Renda_Familiar)) &
    (df['Nivel_de_Educacao_Parental'].isin(parental_education))
]

if show_outliers:
    data_for_plot = filtered_df
    title_suffix = "(Com Outliers)"
else:
    data_for_plot = remove_outliers_iqr(filtered_df, 'Nota_Prova')
    title_suffix = "(Sem Outliers)"

bar_fig = px.box(
    data_for_plot,
    x='Envolvimento_Parental',
    y='Nota_Prova',
    color='Renda_Familiar',
    facet_col='Nivel_de_Educacao_Parental',
    labels={
        'Envolvimento_Parental': 'Envolvimento dos Pais',
        'Nota_Prova': 'Nota no Exame',
        'Renda_Familiar': 'Renda Familiar',
        'Nivel_de_Educacao_Parental': 'Escolaridade dos Pais'
    },
    title=f"Distribuição das Notas {title_suffix}"
)

bar_fig.update_layout(height=500)
st.plotly_chart(bar_fig, use_container_width=True)


st.markdown("---")  


st.subheader("🌀 Apresento o Gráfico de Dispersão de Notas Fatores Familiares")
st.write("Utilize os filtros para ajustar o gráfico conforme desejado.")

col1, col2, col3 = st.columns(3)
with col1:
    Envolvimento_Parental_2 = st.multiselect(
        "Envolvimento dos Pais",
        options=df['Envolvimento_Parental'].unique(),
        default=df['Envolvimento_Parental'].unique(),
        key="parental_involvement_2"  #segunda chave unica fazendo a mesma coisa que a primeira 
    )
with col2:
    Renda_Familiar_2 = st.multiselect(
        "Renda Familiar",
        options=df['Renda_Familiar'].unique(),
        default=df['Renda_Familiar'].unique(),
        key="family_income_2"  
    )
with col3:
    parental_education_2 = st.multiselect(
        "Escolaridade dos Pais",
        options=df['Nivel_de_Educacao_Parental'].unique(),
        default=df['Nivel_de_Educacao_Parental'].unique(),
        key="parental_education_2" 
    )

filtered_df_2 = df[
    (df['Envolvimento_Parental'].isin(Envolvimento_Parental_2)) &
    (df['Renda_Familiar'].isin(Renda_Familiar_2)) &
    (df['Nivel_de_Educacao_Parental'].isin(parental_education_2))
]

fig = px.scatter(
    filtered_df_2,
    x='Envolvimento_Parental',
    y='Nota_Prova',
    color='Renda_Familiar',
    size='Nota_Prova',
    hover_data=['Nivel_de_Educacao_Parental', 'Horas_Estudadas', 'Presenca'],
    facet_col='Nivel_de_Educacao_Parental',
    labels={
        'Envolvimento_Parental': 'Envolvimento dos Pais',
        'Nota_Prova': 'Nota no Exame',
        'Renda_Familiar': 'Renda Familiar',
        'Nivel_de_Educacao_Parental': 'Escolaridade dos Pais'
    },
    title="Nota no Exame vs Envolvimento dos Pais"
)

#st.caption("obs: Nao consegui unir os 2 e um grafico so")

fig.update_layout(height=500)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("🍩 Aprensendo o Pie(Rosquinha) mostrando o Nível de Educação Parental")

df_educacao = (
    df['Nivel_de_Educacao_Parental']
    .value_counts(normalize=True)
    .reset_index()
    .rename(columns={'Nivel_de_Educacao_Parental': 'educacao', 'proportion': 'percentual'})
)

fig_donut = px.pie(
    df_educacao,
    values='percentual',
    names='educacao',
    hole=0.5,
    title='Distribuição da Educação dos Pais',
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig_donut.update_traces(textinfo='percent+label')

st.plotly_chart(fig_donut, use_container_width=True)
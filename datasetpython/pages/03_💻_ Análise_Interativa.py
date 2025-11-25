import pandas as pd 
import streamlit as st  
import plotly.express as px
from utils.carrega_dados import carregar_dados,remove_outliers_iqr

df = carregar_dados()



st.title("📊 Análise Interativa — Fatores que Influenciam a Nota da Prova")

st.write("Explore como diferentes variáveis inteiras se relacionam com o **Exam Score**.")

column_labels = {
    "Horas_Estudadas": "Horas Estudadas",
    "Presenca": "Presença",
    "Horas_de_Sono": "Horas de Sono",
    "Notas_Anteriores": "Notas Anteriores",
    "Aulas_Particulares": "Aulas Particulares",
    "Atividade_Fisica": "Atividade Física"
}

selected_label = st.selectbox("Escolha a variável do eixo X:", options=list(column_labels.values()) #pega os labels de column_labels 
)

# Recuperar o nome real da coluna selecionada
x_axis = [col for col, label in column_labels.items() if label == selected_label][0]

df_plot = df.copy()

remove_outliers = st.toggle("Remover Outliers (IQR)", value=False) #remove outlier

if remove_outliers:
    original_count = len(df_plot)
    df_plot = remove_outliers_iqr(df_plot, "Nota_Prova")
    removed_count = original_count - len(df_plot)
    
fig = px.bar(
    df_plot,
    x=x_axis,
    y="Nota_Prova",
    hover_data=df.columns,
    title=f"Relação entre {x_axis} e Nota da Prova",
    
)

fig.update_layout(
    xaxis_title=x_axis,
    yaxis_title="Nota da Prova",
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

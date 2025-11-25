import pandas as pd 
import streamlit as st
import plotly.figure_factory as ff
import requests

@st.cache_data
def carregar_dados():
    df_original = pd.read_csv('./datasetpython/dataset/StudentPerformanceFactors.csv')
    
    df = pd.DataFrame()
    df['Horas_Estudadas'] = df_original['Hours_Studied']
    df['Presenca'] = df_original['Attendance']
    df['Envolvimento_Parental'] = df_original['Parental_Involvement']
    df['Acesso_a_Recursos'] = df_original['Access_to_Resources']
    df['Atividades_Extracurriculares'] = df_original['Extracurricular_Activities']
    df['Horas_de_Sono'] = df_original['Sleep_Hours']
    df['Notas_Anteriores'] = df_original['Previous_Scores']
    df['Nivel_de_Motivacao'] = df_original['Motivation_Level']
    df['Acesso_a_Internet'] = df_original['Internet_Access']
    df['Aulas_Particulares'] = df_original['Tutoring_Sessions']
    df['Renda_Familiar'] = df_original['Family_Income']
    df['Qualidade_do_Professor'] = df_original['Teacher_Quality']
    df['Tipo_de_Escola'] = df_original['School_Type']
    df['Influencia_dos_Pares'] = df_original['Peer_Influence']
    df['Atividade_Fisica'] = df_original['Physical_Activity']
    df['Dificuldades_de_Aprendizagem'] = df_original['Learning_Disabilities']
    df['Nivel_de_Educacao_Parental'] = df_original['Parental_Education_Level']
    df['Distancia_de_Casa'] = df_original['Distance_from_Home']
    df['Genero'] = df_original['Gender']
    df['Nota_Prova'] = df_original['Exam_Score']
    
    df['Genero'] = df['Genero'].replace({'Female': 'Feminino'})
    df['Genero'] = df['Genero'].replace({'Male': 'Masculino'})
    df['Envolvimento_Parental'] = df['Envolvimento_Parental'].fillna('Não informado')
    df['Envolvimento_Parental'] = df['Envolvimento_Parental'].replace({'Low': 'Baixo'})
    df['Envolvimento_Parental'] = df['Envolvimento_Parental'].replace({'Medium': 'Medio'})
    df['Envolvimento_Parental'] = df['Envolvimento_Parental'].replace({'High': 'Alto'})
    df['Renda_Familiar'] = df['Renda_Familiar'].replace({'Low': 'Baixo'})
    df['Renda_Familiar'] = df['Renda_Familiar'].replace({'Medium': 'Medio'})
    df['Renda_Familiar'] = df['Renda_Familiar'].replace({'High': 'Alto'})
    df['Nivel_de_Educacao_Parental'] = df['Nivel_de_Educacao_Parental'].replace({'High School': 'Ensino Médio'})
    df['Nivel_de_Educacao_Parental'] = df['Nivel_de_Educacao_Parental'].replace({'College': 'Faculdade'})
    df['Nivel_de_Educacao_Parental'] = df['Nivel_de_Educacao_Parental'].replace({'Postgraduate': 'Pós-graduação'})
    df['Acesso_a_Recursos'] = df['Acesso_a_Recursos'].replace({'Low': 'Baixo'})
    df['Acesso_a_Recursos'] = df['Acesso_a_Recursos'].replace({'Medium': 'Medio'})
    df['Acesso_a_Recursos'] = df['Acesso_a_Recursos'].replace({'High': 'Alto'})
    df['Atividades_Extracurriculares'] = df['Atividades_Extracurriculares'].replace({'Yes': 'Sim'})
    df['Atividades_Extracurriculares'] = df['Atividades_Extracurriculares'].replace({'No': 'Não'})
    df['Nivel_de_Educacao_Parental'] = df['Nivel_de_Educacao_Parental'].fillna('Não informado')
    df['Renda_Familiar'] = df['Renda_Familiar'].fillna('Não informado')

    #print(df.dtypes)
    #print(df.Genero.unique())

    return df

def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return data[(data[column] >= lower) & (data[column] <= upper)]





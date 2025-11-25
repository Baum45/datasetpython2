import streamlit as st
from utils.carrega_dados import carregar_dados

st.set_page_config(
    page_title="Student Performance Insights",
    page_icon="📚",
    layout="wide"
)

df = carregar_dados()

st.markdown(f"""
# 📚 Bem-vindo(a) ao **Student Performance Insights**!

Este aplicativo interativo foi desenvolvido para explorar e visualizar os principais insights sobre o desempenho de estudantes em exames. 
Através de dados detalhados, buscamos responder a perguntas cruciais como:

* **Quais fatores mais impactam o desempenho nos exames?**
* **Como horas de estudo, frequência e sono se correlacionam com as notas?**
* **Existem diferenças significativas por tipo de escola, gênero ou contexto familiar?**

Nosso objetivo é fornecer uma ferramenta clara e intuitiva para que educadores, gestores escolares, pais e estudantes 
possam compreender melhor os fatores que influenciam o sucesso acadêmico e tomar decisões informadas.

---

### Como Navegar:

Utilize o menu de navegação na **barra lateral (esquerda)** para explorar as diferentes seções do aplicativo:

* **Utilize a barra lateral para navegar entre as páginas do aplicativo.**
* **Cada apresenta gráfico para visualizações interativas e análises detalhadas.**

Aproveite a exploração dos dados e descubra insights valiosos para melhorar o desempenho estudantil!

O seu conjunto de dados tem as seguintes dimensões:
- **Linhas:** `{df.shape[0]}`
- **Colunas:** `{df.shape[1]}`

Agradecemos a sua visita e esperamos que encontre informações valiosas aqui!
""")

st.header("Visualização básica disponível")
st.dataframe(df.head(20))








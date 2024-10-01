import streamlit as st
from utilidades import leitura_dados
import plotly.express as px


leitura_dados()

# Define as caracteristicas da pagina
st.set_page_config (
    page_title = "Visão Geral",
    page_icon="🏃🏻‍♀️",
    layout="wide",
)

df_data = st.session_state['dados']['df_data']

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.show()
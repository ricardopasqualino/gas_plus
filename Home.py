import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

from utilidades import leitura_dados

leitura_dados()

st.image('static/logo_my_price.jpg', width=120)
st.write("# Maior app de dados de preços de combustíveis!")
st.markdown(
    "My Price foi feito para você gestor ter acesso aos preços praticados nos postos de todo o pais!"
)


import streamlit as st
from utilidades import leitura_dados

leitura_dados()

# Define as caracteristicas da pagina
st.set_page_config (
    page_title = "Preços",
    page_icon="🏃🏻‍♀️",
    layout="wide",
)

df_data = st.session_state['dados']['df_data']

# TRAZER OS ESTADOS
all_states = df_data["ESTADO"].value_counts().index
state = st.sidebar.selectbox("Selecione o estado:", all_states)
select_state = df_data[df_data["ESTADO"] == state ]

#TRAZER AS CIDADES
all_cities = select_state["MUNICIPIO"].value_counts().index
city = st.sidebar.selectbox("Selecione o cidade:", all_cities)
select_city = df_data[df_data["MUNICIPIO"] == city ]

df0 = df_data[(df_data["MUNICIPIO"] == city)]

#TRAZER OS BAIRROS
all_bairros = select_city["BAIRRO"].value_counts().index
bairro = st.sidebar.selectbox("Escolha o Bairro:", all_bairros)
select_bairro = select_city[(select_city["BAIRRO"] == bairro)]

df1 = df0[(df0["BAIRRO"] == bairro)]

#TRAZER OS PRODUTOS
all_products = select_bairro["PRODUTO"].value_counts().index
product = st.sidebar.selectbox("Selecione o Produto:", all_products)
select_product = df1[(df1["PRODUTO"] == product)]

df_filtered = df1[(df1["PRODUTO"] == product)]

# st.sidebar.selectbox('Tipo de consulta', 
#                      ['Base ANP', 'Manual']
#                      )

columns = [
    "RAZAO", 
    "PRECO DE REVENDA", 
    "BANDEIRA",
    "PRODUTO", 
    "UNIDADE DE MEDIDA",
    "DATA DA COLETA", 
    # "MUNICIPIO", 
    # "FANTASIA",
    # "ESTADO", 
    # "BAIRRO", 
]

# Sidebar de produtos

 ### DASHBOARD ###
# Métrica de preço
preco_min = df_filtered['PRECO DE REVENDA'].min()
preco_max = df_filtered['PRECO DE REVENDA'].max()
ultima_atualizacao = df_filtered['DATA DA COLETA'].max()


col1, col2, col3, col4 = st.columns(4)
col1.image('static/logo_my_price.jpg', width=90)
col2.metric(" ## Menor preço", preco_min)
col3.metric(" ## Maior Preço", preco_max)
col4.metric(" ## Última atualização:", ultima_atualizacao)
st.divider()

st.dataframe(df_filtered[columns])

import streamlit as st 
from utilidades import leitura_dados
from datetime import datetime


# Define as caracteristicas da pagina
st.set_page_config (
    page_title = "Add",
    page_icon="🏃🏻‍♀️",
    layout="wide",
)

leitura_dados()

df_data = st.session_state['dados']['df_data']

all_bairros = df_data['BAIRRO'].value_counts().index
all_postos = df_data['RAZAO'].value_counts().index

hora_adicionar = datetime.now()


#TRAZER AS CIDADES
all_cities = df_data["MUNICIPIO"].value_counts().index
city = st.sidebar.selectbox("Selecione o cidade:", all_cities)
select_city = df_data[df_data["MUNICIPIO"] == city ]

df0 = df_data[(df_data["MUNICIPIO"] == city)]

#TRAZER OS BAIRROS
all_bairros = select_city["BAIRRO"].value_counts().index
bairro = st.sidebar.selectbox("Escolha o Bairro:", all_bairros)
select_bairro = select_city[(select_city["BAIRRO"] == bairro)]

df1 = df0[(df0["BAIRRO"] == bairro)]

#TRAZER OS POSTOS
all_postos = select_bairro['CNPJ'].value_counts().index
posto = st.sidebar.selectbox("Escolha o Posto:", all_postos)
select_posto = select_bairro[(select_bairro['CNPJ'] == posto)]

df2 = df1[df1['CNPJ'] == posto]

etanol = st.sidebar.number_input('Valor do Etanol', 0,100)
gas_normal = st.sidebar.number_input('Valor do Gasolina Normal', 0,100)
gas_adtiva = st.sidebar.number_input('Valor do Gasolina Aditivada', 0,100)
diesel = st.sidebar.number_input('Valor do Diesel', 0,100)
gnv = st.sidebar.number_input('Valor do GNV', 0,100)

btn_add_price = st.sidebar.button('Incluir Preços', type='primary')

if btn_add_price:
    add_list = [
                city,
                bairro,
                posto,
                etanol,
                gas_normal,
                gas_adtiva,
                diesel,
                gnv
    ]

    # hora_adicionar = datetime.now()

    # df_data.loc[hora_adicionar] = add_list

    #Salvar os dados na planilha csv
    caminho_datasets = st.session_state['caminho_datasets'] 
    df_data.to_csv(caminho_datasets / 'new_register.csv', decimal=',', sep=';' )


btn_clean = st.sidebar.button('Limpar')

st.dataframe(df2)
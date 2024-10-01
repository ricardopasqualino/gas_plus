
from pathlib import Path
import pandas as pd
import streamlit as st


def leitura_dados():
    if "data" not in st.session_state:
        pasta_datasets = Path(__file__).parent / 'datasets'
        df_data = pd.read_csv("datasets/revendas_lpc_2024-09-22_2024-09-28.csv", index_col=0)
        st.session_state['data'] = df_data

        dados = {
            "df_data": df_data
        }

        st.session_state['caminho_datasets'] = pasta_datasets
        st.session_state['dados'] = dados
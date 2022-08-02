import os
import openpyxl
import pandas as pd
import geopandas as gpd
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from pathlib import Path

st.set_page_config(page_title='Population projection QC app R4V', page_icon=':chart_with_upwards_trend:', layout='wide')


# Load assets

def load_lottie_animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


animation = load_lottie_animation('https://assets2.lottiefiles.com/packages/lf20_16nllt42.json')


# App logic
def CheckFieldsCompliancy(template_dataframe, country_dataframe):
    column_headers_a = list(template_dataframe.columns.values)
    column_headers_b = list(country_dataframe.columns.values)
    diff_a = set(column_headers_a).difference(set(column_headers_b))
    diff_b = set(column_headers_b).difference(set(column_headers_a))
    return st.write(diff_a.to_frame(), diff_b.to_frame())


# Header
with st.container():
    st.subheader('Web application for quality control population projection data RMRP 2023/2024')
    st.title('QC Projection data RMRP 2023/2024')
    st.write('This app will help to develop a QC to population projections per country RMRP')
    st.write('[learn more>](https://r4v.info)')

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Load population projection data')
        country_data = st.file_uploader(label='Load data from excel template', accept_multiple_files=False)
        if country_data is None:
            pass
        else:
            df_country_data = pd.read_excel(country_data, engine='openpyxl', )
    with right_column:
        st_lottie(animation, height=300, key='coding')

Template_file_path = os.getcwd() + '/Template_Population_projections_2023-24.xlsx'
df_template_projections = pd.read_excel(Template_file_path, engine='openpyxl', )

if country_data is None:
    pass
else:
    if st.button('Run QC script'):
        result = CheckFieldsCompliancy(df_template_projections, df_country_data)

import pandas as pd
import geopandas as gpd
import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title='Population projection QC app R4V', page_icon=':chart_with_upwards_trend:', layout='wide')
# Load assets

def load_lottie_animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


animation = load_lottie_animation('https://assets2.lottiefiles.com/packages/lf20_16nllt42.json')
# Header
with st.container():
    st.subheader('Web application for quality control population projection data RMRP 2023/2024')
    st.title('QC Projection data RMRP 2023/2024')
    st.write('This app will hel to develop a QC to population projections per country RMRP')
    st.write('[learn more>](https://r4v.info)')

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Cargar datos')
        st.file_uploader(label='Load data from excel template',accept_multiple_files=False)
    with right_column:
        st_lottie(animation, height=300, key='coding')

excel_url = 'https://www.r4v.info/sites/default/files/2022-06/Template_Population_projections_2023-24.xlsx'
r = requests.get(excel_url)
open('temp.xls', 'wb').write(r.content)
df = pd.read_excel('temp.xls')
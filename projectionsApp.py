import streamlit as st

st.set_page_config(page_title='Population projection QC app R4V', page_icon=':chart_with_upwards_trend:', layout='wide')

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
        st.header('Cargar datos 2')
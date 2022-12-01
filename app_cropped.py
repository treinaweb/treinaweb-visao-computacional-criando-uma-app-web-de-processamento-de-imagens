import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image

st.title("Corta Imagem")

img_file = st.sidebar.file_uploader(label="Envie uma Imagem", type=['png','jpg'])
realtime_update = st.sidebar.checkbox("Atualização em Tempo Real", value=True)
box_color = st.sidebar.color_picker(label="Grupo de Cores", value="#0000FF")
aspect_choice = st.sidebar.radio(label="Proporção da Tela", options=["1:1", "16:9", "4:3"])


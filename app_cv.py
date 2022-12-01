import cv2
import streamlit as st
from PIL import Image
import numpy as np
from skimage import morphology, io, color, feature, filters

def principal():
    st.title("OpenCV Data App")
    st.subheader("Esse aplicativo web permite integrar processamento de imagens")
    st.text("Streamlit com OpenCV")

    arquivo_imagem = st.file_uploader("Envie sua imagem", type=["jpg", "png", "jpeg"])

    taxa_borrao = st.sidebar.slider("Borrão", min_value=0.2, max_value=3.5)
    qtd_brilho = st.sidebar.slider("Brilho", min_value=-50, max_value=50, value=0)
    filtro_aprimoramento = st.sidebar.checkbox("Melhorar Detalhes da Imagem")

    
if __name__ == '__main__':
    principal()
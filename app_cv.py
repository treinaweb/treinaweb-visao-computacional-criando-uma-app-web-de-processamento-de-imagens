import cv2
import streamlit as st
from PIL import Image
import numpy as np
from skimage import morphology, io, color, feature, filters

def brilho_imagem(imagem, resultado):
    img_brilho = cv2.convertScaleAbs(imagem, beta=resultado)
    return img_brilho

def borra_imagem(imagem, resultado):
    img_borrada = cv2.GaussianBlur(imagem, (7,7), resultado)
    return img_borrada

def melhora_detalhe(imagem):
    img_melhorada = cv2.detailEnhance(imagem, sigma_s=35, sigma_r=0.50)
    return img_melhorada

def escala_cinza(imagem):
    img_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    return img_cinza

def principal():
    st.title("OpenCV Data App")
    st.subheader("Esse aplicativo web permite integrar processamento de imagens")
    st.text("Streamlit com OpenCV")

    arquivo_imagem = st.file_uploader("Envie sua imagem", type=["jpg", "png", "jpeg"])

    taxa_borrao = st.sidebar.slider("Borrão", min_value=0.2, max_value=3.5)
    qtd_brilho = st.sidebar.slider("Brilho", min_value=-50, max_value=50, value=0)
    filtro_aprimoramento = st.sidebar.checkbox("Melhorar Detalhes da Imagem")

    img_cinza = st.sidebar.checkbox("Converter para Escala de Cinza")
    img_erosao = st.sidebar.checkbox("Utilizar Filtro Erosão")
    img_dilatacao = st.sidebar.checkbox("Utilizar Filtro Dilatação")
    img_edge = st.sidebar.checkbox("Utilizar Filtro Edge")

    if not arquivo_imagem:
        return None

    imagem_original = Image.open(arquivo_imagem)
    imagem_original = np.array(imagem_original)

    imagem_processada = brilho_imagem(imagem_original, qtd_brilho)
    imagem_processada = borra_imagem(imagem_processada, taxa_borrao)

    if filtro_aprimoramento:
        imagem_processada = melhora_detalhe(imagem_processada)

    if img_cinza:
        imagem_processada = escala_cinza(imagem_processada)

    if img_erosao:
        imagem_processada = morphology.erosion(imagem_processada)

    if img_dilatacao:
        imagem_processada = morphology.dilation(imagem_processada)

    if img_edge:
        imagem_processada = filters.sobel(imagem_processada)

    st.text("Imagem Original")

    st.image(imagem_original)

    st.text("Imagem Processada")

    st.image(imagem_processada)

if __name__ == '__main__':
    principal()
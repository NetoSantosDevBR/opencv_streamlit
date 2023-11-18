import cv2
import streamlit as st
from PIL import Image 
import numpy as np

#Funções
def brilho_imagem(imagem, resultado):
    img_brilho = cv2.convertScaleAbs(imagem, beta=resultado)
    return img_brilho
def borra_imagem(imagem, resultado):
    img_borrada = cv2.GaussianBlur(imagem, (7,7), resultado)
    return img_borrada

def melhora_detalhe(imagem):
    img_melhorada = cv2.detailEnhance(imagem, sigma_s=34, sigma_r=0.50)
    return img_melhorada

#Função principal    
def principal():
    st.title('OpenCV Data App')
    st.subheader('Esse aplicativo web permite integrar processamento de imagens com OpenCV')
    st.text('Streamlit com OpenCV')

    arquivo_imagem = st.file_uploader('Envie sua Imagem', type=['jpg', 'png', 'jpeg'])
    
    taxa_borrao = st.sidebar.slider("Borrão", min_value=0.2, max_value=3.5)
    qtd_brilho = st.sidebar.slider("Brilho", min_value=-50, max_value=50, value=0)
    filtro_aprimoramento =  st.sidebar.checkbox("Melhorar Detalhe da Imagem")
    
    if not arquivo_imagem:
        return None

    imagem_original = Image.open(arquivo_imagem)
    imagem_original = np.array(imagem_original)
    imagem_processada = borra_imagem(imagem_original, taxa_borrao)
    imagem_processada = brilho_imagem(imagem_processada, qtd_brilho)
    
    if filtro_aprimoramento:
        imagem_processada = melhora_detalhe(imagem_processada)
    st.text("Imagem Original vs Imagem Processada")
    st.image([imagem_original, imagem_processada])


if __name__== '__main__':
    principal()   
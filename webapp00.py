# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *


# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Bem vindo/a ao meu primeiro WebApp :) ")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Mentoria do Prof. Massaki")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Ele prefere Python, que crime....")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

values = st.slider("Select a range of values", 0.0, 50.0, (5.0, 15.0))
st.write("Values:", values)

st.image("images.jpg", caption="Sunrise by the mountains")
page_bg_img = "images.jpg"


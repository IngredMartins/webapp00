import streamlit as st
import urllib.parse

# Lista de contatos
listaDeContatos = {
    "Ingred": "+5511944701187",
    "Gabriel": "+5511945329796",
    "Pedro": "+5511950815157"
}

# Função de boas-vindas com HTML personalizado
def boas_vindas():
    st.markdown("""
    <style>
    .title {
        color: #2C3E50;
        font-size: 36px;
        font-weight: bold;
    }
    .subtitle {
        color: #16A085;
        font-size: 24px;
    }
    .description {
        font-size: 18px;
        color: #7F8C8D;
    }
    </style>
    <div class="title">Assistente para Idosos</div>
    <div class="subtitle">Bem-vindo! Escolha uma das opções abaixo.</div>
    <div class="description">Este assistente foi projetado para tornar a comunicação mais fácil.</div>
    """, unsafe_allow_html=True)

# Ligar via WhatsApp com HTML
def ligar_contato_whatsapp():
    contato_selecionado = st.selectbox("Selecione um contato:", [f"{nome} ({numero})" for nome, numero in listaDeContatos.items()])
    contato_numero = listaDeContatos[contato_selecionado.split(' (')[0]]
    
    # Criar URL do WhatsApp
    whatsapp_url = f"https://wa.me/{contato_numero}"

    if st.button("Ligar pelo WhatsApp"):
        st.markdown(f"""
        <a href="{whatsapp_url}" target="_blank" style="background-color: #16A085; padding: 10px 20px; color: white; border-radius: 5px; text-decoration: none; font-size: 18px;">Clique aqui para ligar pelo WhatsApp</a>
        """, unsafe_allow_html=True)

# Função principal
def main():
    boas_vindas()
    opcao = st.selectbox("O que você gostaria de fazer?", ["Ligar para um Contato via WhatsApp"])
    if opcao == "Ligar para um Contato via WhatsApp":
        ligar_contato_whatsapp()

if __name__ == '__main__':
    main()

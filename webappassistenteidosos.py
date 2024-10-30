import streamlit as st

# Função para a tela de boas-vindas
def tela_boas_vindas():
    st.title("Assistente para Idosos")
    st.write("Bem-vindo! Escolha uma das opções abaixo para começar.")

# Função para ligar para um contato (simulação)
def ligar_contato():
    st.subheader("Ligar para um Contato")
    contato = st.selectbox("Selecione um contato:", ["Massaki", "Amadeu", "Gabriel", "Pedro"])
    if st.button("Ligar"):
        st.success(f"Simulando ligação para {contato}...")  # Simula a ação de ligar

# Função para enviar uma mensagem (simulação)
def enviar_mensagem():
    st.subheader("Enviar Mensagem")
    contato = st.selectbox("Selecione um contato para enviar mensagem:", ["Ana", "João", "Maria", "Pedro"])
    mensagem = st.text_area("Digite a mensagem:")
    if st.button("Enviar"):
        if mensagem:
            st.success(f"Mensagem enviada para {contato}: {mensagem}")  # Simula o envio da mensagem
        else:
            st.error("Por favor, digite uma mensagem antes de enviar.")

# Função para navegar na internet
def navegar_internet():
    st.subheader("Navegar na Internet")
    url = st.text_input("Digite o site que deseja visitar (ex: www.google.com):")
    if st.button("Navegar"):
        if url:
            st.success(f"Simulando a abertura do site {url}...")  # Simula a navegação
        else:
            st.error("Por favor, insira um URL válido.")

# Função para usar a câmera
def usar_camera():
    st.subheader("Usar a Câmera")
    picture = st.camera_input("Tirar uma foto")
    if picture:
        st.image(picture)

# Função principal que controla a navegação
def main():
    tela_boas_vindas() 
    
    # Menu de opções
    opcao = st.selectbox("O que você gostaria de fazer?", 
                         ["Ligar para um Contato", 
                          "Enviar uma Mensagem", 
                          "Navegar na Internet", 
                          "Usar a Câmera"])
      
    # Chamar a função correta com base na escolha do usuário
    if opcao == "Ligar para um Contato":
        ligar_contato()
    elif opcao == "Enviar uma Mensagem":
        enviar_mensagem()
    elif opcao == "Navegar na Internet":
        navegar_internet()
    elif opcao == "Usar a Câmera":
        usar_camera()

# Execução do aplicativo
if __name__ == '__main__':
    main()

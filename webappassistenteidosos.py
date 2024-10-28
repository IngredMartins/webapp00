import streamlit as st

# Função para a tela de boas-vindas
# def é para definir uma função
def tela_boas_vindas():
    st.title("Assistente para Idosos")
    st.write("Bem-vindo! Escolha uma das opções abaixo para começar.")

# Função para ligar para um contato
def ligar_contato():
    st.subheader("Ligar para um Contato")
    contato = st.selectbox("Selecione um contato:", ["Massaki", "Amadeu", "Gabriel", "Pedro"])
    if st.button("Ligar"):
        st.success(f"Ligando para {contato}...")

# Função para enviar uma mensagem
def enviar_mensagem():
    st.subheader("Enviar Mensagem")
    contato = st.selectbox("Selecione um contato para enviar mensagem:", ["Ana", "João", "Maria", "Pedro"])
    mensagem = st.text_area("Digite a mensagem:")
    if st.button("Enviar"):
        client = plivo.RestClient('<auth_id>','<auth_token>') 
        response = client.messages.create( 
        src='<sender_number>')
        dst='<destination_number>'           
        text="Hello, world"')'
        
# Função para navegar na internet
def navegar_internet():
    st.subheader("Navegar na Internet")
    url = st.text_input("Digite o site que deseja visitar (ex: www.google.com):")
    if st.button("Navegar"):
        if url:
            st.success(f"Abrindo o site {url}...")
        else:
            st.error("Por favor, insira um URL válido.")

# Função para usar a câmera
def usar_camera():
    st.subheader("Usar a Câmera")
    if st.button("Tirar Foto"):
    if picture:
    st.image(picture)
        # Aqui, poderia ser implementada a funcionalidade de tirar uma foto real, se necessário

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

#Função mensagem na tela
import plivo 
client = plivo.RestClient('<auth_id>','<auth_token>')
response = client.messages.create( src='<sender_number>', dst='<destination_number>', text='Hello, world!',) 
print(response)

# Execução do aplicativo
if __name__ == '__main__':
    main()

import streamlit as st
import urllib.parse  # biblioteca de url


def boas_vindas():
    st.title("Bem-vindo ao Assistente inteligente para Idosos")

# Função principal da navegação
def main():
    boas_vindas()     
    
    opcao = st.selectbox("O que você gostaria de fazer?", 
                         ["Ligação via WhatsApp", 
                          "Mensagem via WhatsApp", 
                          "Acessar a Internet", 
                          "Tirar uma foto"])
      
    if opcao == "Ligar para um Contato via WhatsApp":
        ligar_contato_whatsapp()
    elif opcao == "Enviar uma Mensagem via WhatsApp":
        enviar_mensagem_whatsapp()
    elif opcao == "Navegar na Internet":
        navegar_internet()
    elif opcao == "Usar a Câmera":
        usar_camera()

listaDeContatos = {
    "Ingred": "+5511944701187",
    "Gabriel": "+5511945329796",
    "Pedro": "+5511950815157"
}

def ligar_contato_whatsapp():
    st.subheader("Ligar para alguém via WhatsApp")
    contato_selecionado = st.selectbox("Para quem quer ligar hoje ?:", [f"{nome} ({numero})" for nome, numero in listaDeContatos.items()])
    
    # Extrair o número do contato selecionado
    contato_numero = listaDeContatos[contato_selecionado.split(' (')[0]]  # Pega apenas o nome antes de ' ('
    
    if st.button("Ligar pelo WhatsApp"):
        whatsapp_url = f"https://wa.me/{contato_numero}"
        st.markdown(f"[Clique aqui para ligar pelo WhatsApp]({whatsapp_url})")


# Função para enviar uma mensagem via WhatsApp
def enviar_mensagem_whatsapp():
    st.subheader("Enviar Mensagem via WhatsApp")
    contato_selecionado = st.selectbox("Selecione um contato para enviar mensagem:", [f"{nome} ({numero})" for nome, numero in listaDeContatos.items()])
    
    # Extrair o número do contato selecionado
    contato_numero = listaDeContatos[contato_selecionado.split(' (')[0]]  # Pega apenas o nome antes de ' ('
    
    mensagem = st.text_area("Digite a mensagem:")
    
    if st.button("Enviar"):
        if mensagem:
            # Codificar a mensagem para URL
            mensagem_codificada = urllib.parse.quote(mensagem)
            whatsapp_url = f"https://wa.me/{contato_numero}?text={mensagem_codificada}"
            st.markdown(f"[Clique aqui para enviar a mensagem pelo WhatsApp]({whatsapp_url})")
        else:
            st.error("Por favor, digite uma mensagem antes de enviar.")


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
    picture = st.camera_input("Tirar uma foto")
    if picture:
        st.image(picture)





# Execução do aplicativo
if __name__ == '__main__':
    main()

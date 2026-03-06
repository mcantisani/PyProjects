# PROJETO CHATBOT COM IA
#  Nesse projeto vamos criar um site com chatbot que responde perguntas com a ajuda de um modelo de IA como o ChatGPT. 
# O próximo passo é escolher o framework para criar o site. Existem várias opções, como Flask, Django, Streamlit, FastAPT etc.
# Para este projeto, vamos usar o Streamlit, que é simples e com o Python conseguimos criar o frontend e o backend no mesmo framework.
# A IA que vamos usar para responder as perguntas do usuário será o ChatGPT, que é um modelo de linguagem desenvolvido pela OpenAI.
# Para usar o ChatGPT, precisamos instalar a biblioteca OpenAI e obter uma chave de API da OpenAI. Você pode se inscrever para uma conta gratuita e obter sua chave de API no site da OpenAI.
# Depois de obter a chave de API, podemos usar a biblioteca OpenAI para enviar perguntas para o ChatGPT e receber respostas. 
# O código a seguir é um exemplo de como criar um chatbot simples usando Streamlit e a API do ChatGPT:

import streamlit as st
from openai import OpenAI


modelo_ia = OpenAI(api_key="insira sua chave de API aqui")
# O site deverá ter um títulol intuitivo
st.title("MagaGPT - O seu assistente virtual inteligente")
st.write("Digite sua pergunta para o MagaGPT.")

#logica para armazenar o histórico de mensagens
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = [] #[{"role": "system", "content": "Você é um assistente útil e amigável. Você vai responder de forma concisa."}] #mensagem inicial do sistema, que pode dar contexto para o modelo de IA

# O site deverá ter um campo de input para o usuário digitar suas perguntas
pergunta_usuario = st.chat_input("Digite sua pergunta aqui:")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

# O site deverá exibir a pergunta que o usuário inputou no campo de input, guardando o histórico das conversas.
if pergunta_usuario:
    st.chat_message("user").write(pergunta_usuario) #human -> usuário, assistant -> IA
    mensagem_usuario = {"role": "user", "content": pergunta_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    
    # resposta do ChatGPT
    resposta_obj = modelo_ia.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state["lista_mensagens"],
    )
    # extrai o texto retornado
    resposta_ia = resposta_obj.choices[0].message.content
    st.chat_message("assistant").write(resposta_ia)
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ia})
    #st.file_uploader("Faça upload de um arquivo para o MagaGPT analisar
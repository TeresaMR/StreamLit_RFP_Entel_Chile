import streamlit as st
##from hugchat import hugchat

# Import Langchain interface  and use base chain
from watsonxga import WatsonxLangchainLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
import ClientDiscoveryState as clientDiscoveryState
import utilfunctions as utils
import os
#Configurations for webpage
st.set_page_config(page_title="Procesador de RFP",page_icon="src/img/entel_icon.png")


##Sesión
# Store LLM generated responses
#user->user'input and bot-> bot response.
    # Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []



##contenido pagina
##Titulos
st.title('PROCESAR RFP')
st.write('Esta interfaz es una demostración de cómo implementar Watsonx.ia para dar escalabilidad a las soluciones de IA Generativa!')

##SET BUTTONS WITH QUESTIONS
contBtn=st.container()

with contBtn:
     ###FUNCION BTN ONCLICK 
    row1 = st.columns(3)
    i=0
    btnArray=["Sobre RFP","Puntos Clave","Nuevo"]
    nombre=""
    for col in row1:
        tile = col.container(height=40,border=False)
        nombre = btnArray[i]
        btn=tile.button(label=nombre,on_click=utils.btnfunction(nombre))
        i+=1
        







##Set Chat 
with st.chat_message("iabot"):
    st.write("¿En qué te puedo ayudar? 👋")

prompt = st.chat_input("Preguntame sobre el documento.")
if prompt:
    #st.write(f"User has sent the following prompt: {prompt}")
    with st.spinner("Pensando..."):
           # client=clientDiscoveryState()
            response = clientDiscoveryState.ClientDiscoveryState.on_button_click(clientDiscoveryState,prompt)
            #st.write(response) 
            with st.chat_message("iabot"):
                st.markdown(response)




##Sidebar 
with st.sidebar:
    st.title('Índice del documento')
    with st.spinner("Pensando..."):
          
           prompt="Hazme un indice de temas del documento"
           response = clientDiscoveryState.ClientDiscoveryState.on_button_click(clientDiscoveryState,prompt)
           
           st.divider()
           responseLimpia1,response2=response.split("propuesta_test[93].docx",1)
          # st.write()
           i = 0 
           res = responseLimpia1.split()
           for valor in res:
                
                if "." in valor:
                     proxima=res[i+1]
                     st.write(valor+" "+ proxima)
                     i+=2
                
                     
           
           

                
         
          
           

            



##########################################################################################

# Display chat messages
#for message in st.session_state.messages:
  #  with st.chat_message(message["role"]):
     #   st.write(message["content"])

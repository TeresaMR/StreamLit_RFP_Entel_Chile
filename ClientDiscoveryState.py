from watsonxga import WatsonxLangchainLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from prompt import ragprompt 
from discoveryConcect import Discovery 
import os

##LLM Response CLASS
class ClientDiscoveryState():
    question: str = ""
    chat_history: list[tuple[str, str]]
    store_created: bool = True
    file_name: str= "propuesta_test[92].docx"
    is_uploading: bool = True
    prompt: str 
    llm: WatsonxLangchainLLM
    

    

    async def answer(self):
        prompt = ragprompt(self.question, "propuesta_test[92].docx")
        print("usamos  ga")
       
        answer = self.llm(prompt)
        self.chat_history.append(self.question, answer)
                        

    def run_prompt(self, prompt):
        self.question = prompt
        
        prompt = ragprompt(self.question, Discovery.callDiscDocument(prompt))
        print("usamos  ga")

        llm = WatsonxLangchainLLM(
            model_id="ibm-mistralai/mixtral-8x7b-instruct-v01-q",
            generate_params={
            GenParams.DECODING_METHOD: "greedy",
            GenParams.MAX_NEW_TOKENS: 200,
                },
         ).from_pretrained()
        
       
        answer = llm(prompt)
        #print(answer)
        return answer 
        #self.chat_history.append(self.question, answer)
        

    def on_button_click(self, pregunta):
            ClientDiscoveryState.prompt=pregunta
            
            ClientDiscoveryState.question=ClientDiscoveryState.prompt
            print("la pregunta es:   ")
            print(ClientDiscoveryState.question)
           # ClientDiscoveryState.run_prompt(self,pregunta)
            return ClientDiscoveryState.run_prompt(self,pregunta)
         

    def clear_state(self):
        self.question = ""
        self.chat_history = []
        self.store_created = True


   

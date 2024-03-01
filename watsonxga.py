
import streamlit as st

from pydantic import BaseModel
# Import IBM Gen 
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM

class WatsonxLangchainLLM(BaseModel): 
    
    generate_params: dict = { GenParams.MAX_NEW_TOKENS: 59349 }

    model_id: str = "ibm-mistralai/mixtral-8x7b-instruct-v01-q"


    def from_pretrained(self):

        model = Model(
            model_id=self.model_id,
            credentials={
                "apikey": "inhUiWOKqsAN9UURCOdSEoZ7zhUnQayptqpQTOSiozPN",
                "url": "https://us-south.ml.cloud.ibm.com"
            },
            params=self.generate_params,
            project_id="112ec648-a09b-4625-a4eb-c625fff4ff91"
        )

        llm = WatsonxLLM(model=model)
        return llm 

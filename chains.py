import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.2-11b-vision-preview")

    def write_res(self, text_input):
        prompt_res = PromptTemplate.from_template(
           "{text_input}"
        )
        chain_res = prompt_res | self.llm
        res = chain_res.invoke({"text_input": text_input})
        return res.content
    
        

import openai
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

load_dotenv(dotenv_path="enviornment.env")

secret_key = os.getenv('OPENAI_API_KEY')

os.environ["OPENAI_API_KEY"] = secret_key

def practice():
    prompt = PromptTemplate.from_template("What is the capital of India?")
    
    llm = OpenAI(temperature=0.3)
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    output = chain.run({}) 
    print(output)

practice()


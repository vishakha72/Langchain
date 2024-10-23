from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI  # Correct import for OpenAI model
from langchain.chains import LLMChain
import os

os.environ["OPENAI_API_KEY"] = "YOUR_SECRET_KEY"

def practice():
    prompt = PromptTemplate.from_template("What is the capital of {place}?")
    
    # Set up the OpenAI LLM with desired temperature
    llm = OpenAI(temperature=0.3)
    
    # Create an LLMChain with the LLM and the prompt
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # Define the place to inquire about
    city = "New York City" #You can skip this as we already are specific about the place so in case of {place} you can directly write the place
    
    # Run the chain and get the result
    output = chain.run(city) 
    print(output)

practice()

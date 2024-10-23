#In this we are using Ollama open source 
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

llm = ChatAnthropic(model='claude-2')
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
llm = ChatOllama(model="llama2-7b")

result = llm.invoke("How can I schedule my day?")

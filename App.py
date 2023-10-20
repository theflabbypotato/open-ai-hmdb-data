import os

import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.llms import HuggingFacePipeline

from langchain.document_loaders.csv_loader import CSVLoader


#Tried HuggingFace as well
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
# Put your own API Keys here:
# https://platform.openai.com/account/api-keys 
# ^ for openai to make your own free api key

os.environ['OPENAI_API_KEY'] = ""
os.environ['HUGGINGFACEHUB_API_TOKEN'] =''

# APP
# Have to run
st.title("HMDB Serum Inquiry")

user_csv1 = st.file_uploader("Upload your CSV file", type="csv")
user_csv2 = st.file_uploader("Optional: Upload your second CSV file", type="csv")


if user_csv1 is not None:
    question = st.text_input("Ask your question here: ")
    
    #LLMS
    llm = OpenAI(temperature=0)
    #llm = HuggingFacePipeline(temperature=0)
    if user_csv2 is not None:
        agent = create_csv_agent(llm, [user_csv1, user_csv2], verbose=True)
        #running code by itself so can be dangerous
        
        if question is not None and question != "":
            response = agent.run(question)
            st.write(response)
        
    else:
        agent = create_csv_agent(llm, user_csv1, verbose=True)
        #running code by itself so can be dangerous
        
        if question is not None and question != "":
            response = agent.run(question)
            st.write(response)
    
    

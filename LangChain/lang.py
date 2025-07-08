from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI 
from langchain_core.runnables import Runnable


import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")


template = """
You are a helpful assistant. Use the context below to answer the question.

Context:
{text}

Question:
{question}

Answer:"""
prompt = PromptTemplate.from_template(template)


llm = OpenAI(temperature=0, openai_api_key=api_key)


chain: Runnable = prompt | llm


context = """
LangChain is a framework designed to simplify working with language models.
It provides tools to build chains of calls to LLMs and other utilities.
"""
question = "What is LangChain?"


response = chain.invoke({"text": context, "question": question})
print("Answer:", response)

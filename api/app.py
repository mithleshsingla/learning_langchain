
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
load_dotenv()


app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

#ollama llama2
llm1=OllamaLLM(model="qwen2.5:0.5b")

##ollama llama2
llm2=OllamaLLM(model="qwen2.5:0.5b")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 50 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 50 words")

add_routes(
    app,
    prompt1|llm1,
    path="/essay"

)

add_routes(
    app,
    prompt2|llm2,
    path="/poem"

)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)


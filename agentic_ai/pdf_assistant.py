import typer
from typing import Optional,List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
from langchain_ollama import OllamaLLM
import os
from dotenv import load_dotenv
load_dotenv()

llm=OllamaLLM(model="qwen2.5:0.5b")
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector2(collection="recipes", db_url=db_url)
)

knowledge_base.load()
storage=PgAssistantStorage(table_name="pdf_assistant", db_url=db_url)

def pdf_assistant(new:bool=False,user:str="user"):
    run_id: Optional[str] = None
    if not new:
        existing_run_ids: List[str] = storage.get_run_ids(user)
        if len(existing_run_ids) > 0:
            run_id = existing_run_ids[0]

    assistant = Assistant(
        llm=llm,
        knowledge_base=knowledge_base,
        storage=storage,
        user=user,
        show_tool_calls=True,
        search_knowledge=True,
        read_chat_history=True,
        run_id=run_id
    )
    if run_id is None:
        run_id=assistant.run_id
        print(f"New run started with ID: {run_id}")
    else:
        print(f"Continuing run with ID: {run_id}")

    assistant.cli_app(markdown=True)        

if __name__ == "__main__":
    typer.run(pdf_assistant)    

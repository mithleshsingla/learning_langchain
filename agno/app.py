from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import   DuckDuckGoTools
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key=os.environ['GROQ_API_KEY']
#llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-8b-8192")


agent=Agent(model=Groq(id="llama3-8b-8192"),description="you are assistant. please reply based on question.",tools=[DuckDuckGoTools()],markdown=True)
agent.print_response("india")
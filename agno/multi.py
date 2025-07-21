from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import   DuckDuckGoTools
import os
from dotenv import load_dotenv
load_dotenv()
from agno.tools.yfinance import YFinanceTools
groq_api_key=os.environ['GROQ_API_KEY']
#llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-8b-8192")


fin_agent=Agent(name="fin agent",role="search web for financial data",model=Groq(id="llama3-8b-8192"),instructions="always include the sources and use tables ",show_tool_calls=True,tools=[YFinanceTools(stock_price=True,analyst_recommendations=True)],markdown=True)

web_agent=Agent(name="web agent",role="search web",model=Groq(id="llama3-8b-8192"),instructions="always include the sources",show_tool_calls=True,tools=[DuckDuckGoTools()],markdown=True)

agent_team=Agent(
    team=[web_agent,fin_agent],
    model=Groq(id="llama3-8b-8192"),
    instructions="always include the sources and use tables ",show_tool_calls=True,
    markdown=True
)










agent_team.print_response("analyse company like google and nvidia, suggest which to buy")
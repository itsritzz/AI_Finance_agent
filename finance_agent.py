import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.googlesearch import GoogleSearch
from phi.tools.duckduckgo import DuckDuckGo
# from phi.model.huggingface import HuggingFaceChat
load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

web_agent = Agent(
    name= "Web Agent",
    model= Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    role= "Search the web for information and print sources",
    tools=[GoogleSearch()],
    # tools=[DuckDuckGo()],
    instructions="ALWAYS include sources and provide relevant news.",
    show_tool_calls=True,
    # debug_mode=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model= Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    role = "Get financial data",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    # tools=[YFinanceTools(enable_all=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    # debug_mode=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    # model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["ALWAYS print summary with sources web url", "Use tables to display data"],
    show_tool_calls=True,
    # debug_mode=True,
    markdown=True,
)
agent_team.print_response("Summarize analyst recommendations and share the latest news from the web for ULTRACEMCO.NS", stream=True)

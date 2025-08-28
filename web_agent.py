import asyncio
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)
search_tool = TavilySearch(max_results=5)

agent = create_react_agent(
    model=llm,
    tools=[search_tool],
)

async def run_query_async(query: str):
    """Async query runner"""
    result = await agent.ainvoke({"messages": [("user", query)]})
    return result["messages"][-1].content

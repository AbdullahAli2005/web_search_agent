# web_agent.py
import os
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

def run_query(query: str):
    """Run a query through LangGraph agent, safe for Streamlit loops."""
    async def _run():
        result = await agent.ainvoke({"messages": [("user", query)]})
        return result["messages"][-1].content

    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():  # Streamlit already has an event loop
            return loop.run_until_complete(_run())
        else:
            return loop.run_until_complete(_run())
    except Exception as e:
        return f"❌ Error: {e}"


if __name__ == "__main__":
    query = "Latest breakthroughs in AI 2025"
    print("🔎 Query:", query)
    print("📄 Answer:", run_query(query))

import asyncio
import nest_asyncio
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent

nest_asyncio.apply()

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)
search_tool = TavilySearch(max_results=5)

agent = create_react_agent(
    model=llm,
    tools=[search_tool],
)

async def _run_query_async(query: str):
    """Async version of run_query"""
    result = await agent.ainvoke({"messages": [("user", query)]})
    return result["messages"][-1].content

def run_query(query: str):
    """Safe sync wrapper for both local & Streamlit"""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # No running loop → safe for CLI
        return asyncio.run(_run_query_async(query))
    else:
        # Already inside Streamlit loop → reuse it
        return loop.run_until_complete(_run_query_async(query))


if __name__ == "__main__":
    query = "Latest breakthroughs in AI 2025"
    print("🔎 Query:", query)
    print("📄 Answer:", run_query(query))

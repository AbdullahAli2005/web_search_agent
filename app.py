import streamlit as st
import asyncio
from web_agent import run_query_async

st.set_page_config(page_title="AI Web Search Agent", page_icon="🌐")

st.title("🌐 AI Web Search Agent")

query = st.text_input("Enter your query:")

if st.button("Search"):
    if query.strip():
        try:
            with st.spinner("🔍 Searching..."):
                # Direct async run
                result = asyncio.run(run_query_async(query))
            st.success("✅ Done!")
            st.write(result)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a query first.")

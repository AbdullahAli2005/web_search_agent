import streamlit as st
from web_agent import run_query

st.set_page_config(page_title="🌐 Web Search Agent", layout="centered")

st.title("🌐 AI Web Search Agent")
query = st.text_input("Enter your query:")

if st.button("Search"):
    if not query.strip():
        st.warning("⚠️ Please enter a query before searching.")
    else:
        with st.spinner("🔎 Searching..."):
            result = run_query(query)
        st.success("✅ Done!")
        st.write(result)

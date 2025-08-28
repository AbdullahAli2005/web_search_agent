import streamlit as st
from web_agent import run_query

st.set_page_config(page_title="AI Web Search Agent", page_icon="🌐")

st.title("🌐 AI Web Search Agent")

query = st.text_input("Enter your query:")

if st.button("Search"):
    if query.strip():
        try:
            with st.spinner("🔍 Searching..."):
                result = run_query(query)
            st.success("✅ Done!")
            st.write(result)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a query first.")

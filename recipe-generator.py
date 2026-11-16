import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

st.set_page_config(page_title="Ask the Chef", page_icon="👨‍🍳")
st.title("👨‍🍳 Ask the Chef")

# Cache the chain so it loads ONCE instead of on every message
@st.cache_resource
def get_chain():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful Head Chef. Give clear, concise recipes with ingredients and numbered steps."),
        ("user", "{question}")
    ])
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    return prompt | llm | StrOutputParser()

chain = get_chain()

# Keep chat messages on screen
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if question := st.chat_input("Ask the Chef for a recipe..."):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        reply = st.write_stream(chain.stream({"question": question}))

    st.session_state.messages.append({"role": "assistant", "content": reply})
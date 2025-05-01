import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(page_title="LangChain Web Search Chatbot", page_icon="🤖", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        .stChatMessage {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            box-shadow: 0px 0px 8px rgba(0,0,0,0.05);
        }
        .stTextInput > div > div > input {
            background-color: #e8f0fe;
        }
        .css-1cpxqw2 {
            color: #3b3b3b;
        }
    </style>
""", unsafe_allow_html=True)

# Title and instructions
st.title("🤖 AI-Agent-Powered Chatbot with Web Search")
st.markdown("Ask me anything! I'll use **Wikipedia**, **arXiv**, and **DuckDuckGo** to get answers from the web.")

# Sidebar for settings
st.sidebar.title("⚙️ Settings")
api_key = st.sidebar.text_input("🔑 Enter your Groq API Key:", type="password")
st.sidebar.markdown("**Tip**: You can get the key from [Groq](https://console.groq.com/)")

# Initialize tools
wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

arxiv_api_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv = ArxivQueryRun(api_wrapper=arxiv_api_wrapper)

search = DuckDuckGoSearchRun(name="Search")

# Session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi! I'm a chatbot who can search the web. 🌐 How can I help you today?"}
    ]

# Display conversation
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt := st.chat_input(placeholder="Try asking: What is machine learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not api_key:
        st.warning("Please enter your Groq API key in the sidebar to continue.")
    else:
        # Initialize LLM and tools
        llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
        tools = [wiki, arxiv, search]
        search_agent = initialize_agent(tools, llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)

        # Show assistant response with spinner
        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            with st.spinner("Searching the web and thinking... 🤔"):
                response = search_agent.run(prompt, callbacks=[st_cb])
                #st.session_state.messages for history or to be aware of the chat history
            st.session_state.messages.append({'role': 'assistant', "content": response})
            st.write(response)

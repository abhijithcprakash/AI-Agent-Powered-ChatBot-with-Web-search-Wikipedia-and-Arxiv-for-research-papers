

```markdown
# 🤖 AI Agent-Powered Chatbot with Web Search, Wikipedia, and arXiv

An interactive chatbot that can **search the web**, **query Wikipedia**, or **fetch research papers from arXiv**, depending on your question — all powered by **LangChain tools and agents**.

This project demonstrates how modern LLMs can:
- Use external tools
- Reason about queries
- Select tools dynamically
- Explain their decision-making process in real time

---

## 🚀 Features

- 🔍 Uses **LangChain Agents** to choose the right tool for each query  
- 🌐 Integrates with **Wikipedia**, **arXiv**, and **DuckDuckGo**  
- 📚 Ideal for both general knowledge and academic research  
- 🧠 Shows the **step-by-step reasoning** process of the agent  
- 💬 Interactive chatbot UI with **Streamlit**  
- 🔐 Powered by **Groq API** using `Llama3-8b-8192`  

---

## 🧠 How It Works

### 1. LLM Configuration

The LLM used is **Llama 3** via Groq API, wrapped using LangChain's `ChatGroq` interface. It supports tool calling and multi-step reasoning.

### 2. Tools Used

- `WikipediaQueryRun`: For factual lookups  
- `ArxivQueryRun`: For academic paper summaries  
- `DuckDuckGoSearchRun`: For general web search  

These tools are connected via LangChain's standardized API wrappers.

### 3. Agent Logic

We use:

```python
AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION
```

This enables the chatbot to:
- Interpret the user's question
- Select a tool
- Take multiple reasoning steps
- Return the final answer with **traceable logic**

### 4. Real-Time Thought Process

For every question, you’ll see:
- **Thought**: What the agent is thinking  
- **Action**: Which tool it chose  
- **Observation**: The tool’s response  
- **Final Answer**: A summarized reply to the user  

This makes it easy to **understand and trust** the AI's decision-making.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/langchain-search-chatbot.git
cd langchain-search-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
pip install streamlit
```

### 3. Add Groq API Key

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
```

Or, enter the key in the sidebar input on the Streamlit UI.

### 4. Launch the App

```bash
streamlit run app.py
```

---

## 🤖 Example Use Case

> **User:** What is the transformer architecture in deep learning?

Output:

```
Thought: The user is asking about a deep learning concept. I will check Wikipedia.
Action: Wikipedia
Action Input: "Transformer (machine learning)"
Observation: The Transformer is a model introduced in the paper "Attention Is All You Need"...
Final Answer: The Transformer is a deep learning architecture based entirely on attention mechanisms...
```

---

## 📌 Notes

- Chat history is preserved for a natural conversation flow  
- You can watch how the AI "thinks" before answering  
- Combines **retrieval-augmented generation (RAG)** with reasoning  

---

## 📄 License

This project is licensed under the MIT License.
```

---

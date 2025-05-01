```markdown
#  🤖 AI-Agent-Powered-ChatBot-with-Web-search-Wikipedia-and-Arxiv-for-research-papers
Made Chat bot which can search web, wikipedia and arxiv depending on the need of the user, LangChain tools and agents are used

A smart, interactive chatbot built with [LangChain](https://www.langchain.com/), powered by **LLM agents** and real-time tools like **Wikipedia**, **arXiv**, and **DuckDuckGo**. This project showcases how modern LLMs can use **external tools**, reason about user queries, and return meaningful answers with traceable "thinking" steps.

---

## 🚀 Features

- 🔍 Uses **LangChain Agents** to dynamically choose the right tool for the query
- 🌐 Integrates with **Wikipedia**, **arXiv**, and **DuckDuckGo** search
- 📚 Answers research-related or general knowledge questions
- 🧠 Displays the agent's **step-by-step reasoning process** in real time
- 🛠️ Built with **Streamlit** for an interactive web interface
- 🔐 Supports **Groq API** and uses the powerful `Llama3-8b-8192` model

---

## 🧠 How It Works

### 1. LLM Setup

This chatbot uses the `ChatGroq` class from `langchain_groq`, powered by Groq’s Llama 3 model. This LLM is capable of following instructions and interacting with LangChain’s tools and agents framework.

### 2. Tools

Three LangChain tools are initialized:

- **WikipediaQueryRun** – to get short summaries from Wikipedia.
- **ArxivQueryRun** – to fetch academic papers and abstracts from arXiv.
- **DuckDuckGoSearchRun** – to search the web for broader queries.

Each tool wraps an API and abstracts its access to fit within LangChain’s agent reasoning loop.

### 3. Agent Configuration

We use:

```
AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION
```

This agent type enables **reasoning and tool use in a step-by-step fashion**. It interprets the user query, thinks about which tools to use, performs the actions, and returns the final answer. If multiple steps are needed, the agent can make several tool calls before answering.

### 4. Reasoning and Thought Process

When you ask a question, you’ll notice:

- The agent **thinks out loud**.
- It evaluates the query and decides which tool to use.
- It executes tool calls (like querying arXiv or Wikipedia).
- It shows intermediate steps like `Thought`, `Action`, `Observation`.
- This gives users a **transparent look into the LLM's reasoning process**.

### 5. Error Handling

If an invalid input is passed (e.g., a list of chat messages instead of a string prompt), the agent may throw a **parsing error**. This has been fixed by ensuring the `run()` method always receives a valid `string` prompt.

---

## 💻 Demo

https://user-app-url.streamlit.app  *(if hosted)*

---

## 🛠️ Installation & Setup

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/langchain-search-chatbot.git
cd langchain-search-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure to also install Streamlit if it's not already installed:

```bash
pip install streamlit
```

### 3. Set Environment Variables

You can either set your **Groq API key** in a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Or enter it directly in the Streamlit sidebar.

### 4. Run the App

```bash
streamlit run app.py
```


## 🤖 Example Usage

> **User:** What is the transformer architecture in deep learning?

You’ll see:

```
Thought: The user is asking about a deep learning concept. I will check Wikipedia.
Action: Wikipedia
Action Input: "Transformer (machine learning)"
Observation: The Transformer is a model architecture introduced in the paper "Attention Is All You Need"...
Final Answer: The Transformer is a deep learning architecture based entirely on attention mechanisms...
```

---

## 📌 Notes

- The chatbot supports **multi-turn conversations**, preserving context.
- You can visually **observe the agent’s decision-making** and how it selects tools.
- This setup demonstrates **how LLMs can be enhanced with retrieval and reasoning**.

---


## 📝 License

This project is open-source and available under the MIT License.

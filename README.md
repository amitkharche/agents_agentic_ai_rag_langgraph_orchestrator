
---

# 🧠 Agentic AI Orchestrator with LangGraph, RAG & Tool-Calling

A production-grade, modular **multi-agent AI system** using **LangGraph**, **OpenAI GPT-4**, **vector search (RAG)** with FAISS, and an intuitive **Streamlit interface**. Designed for intelligent orchestration of complex tasks with modular agents, persistent memory, and tool-augmented reasoning.

---

## 🚀 Overview

This project enables:

* 🤖 **LangGraph-based multi-agent coordination**
* 📚 **Retrieval-Augmented Generation (RAG)** using FAISS
* 🛠️ **Custom tools** like Calculator, Wikipedia, Summarizer
* 🧾 **CSV-based Knowledge Base** for grounding agent responses
* 🖥️ **Streamlit UI** for interactive task input and display

---

## 🔍 Project Highlights

| Feature                    | Description                                                                   |
| -------------------------- | ----------------------------------------------------------------------------- |
| 🧠 LangGraph Framework     | Enables intelligent multi-agent workflows with routing logic                  |
| 📚 Retrieval-Augmented Gen | Uses vector DB (FAISS) + CSV KB for grounded, factual responses               |
| 🧩 Modular Agents          | Includes **Researcher**, **Coder**, **Summarizer**, **Planner**, **QA**, etc. |
| 🧰 Tool Integration        | Wikipedia API, OpenAI summarizer, calculator, and vector store lookup         |
| 🧵 Memory-Aware Dialogue   | Tracks full chat history for context-aware responses                          |
| 🖥️ Streamlit App          | Easy-to-use interface for input/output of agent decisions                     |

---

## 💼 Business Scope

Agentic AI simulates a cross-functional digital workforce. Each agent has a role:

| Agent         | Responsibility                                                              |
| ------------- | --------------------------------------------------------------------------- |
| 🧠 Supervisor | Delegates the task to the appropriate agent                                 |
| 🧪 Researcher | Uses Wikipedia + RAG tool to find and return factual information            |
| 👨‍💻 Coder   | Answers coding problems or generates code via GPT                           |
| 📃 Summarizer | Summarizes large or complex text input                                      |
| 📅 Planner    | Breaks down complex goals into actionable steps                             |
| 📚 Retriever  | Fetches relevant info from a local knowledge base using FAISS vector search |

---

## 🧰 Supported Tools

| Tool Name      | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| WikipediaTool  | Uses `langchain` + `WikipediaAPIWrapper` for real-world facts     |
| SummarizerTool | Leverages GPT-4 to summarize paragraphs or document content       |
| CalculatorTool | Executes basic Python arithmetic from text                        |
| RAGVectorTool  | Loads FAISS vector DB and retrieves top-K matching chunks from KB |

Each tool is independently importable and agent-compatible.

---

## 📁 Project Structure

```
agentic-ai-orchestrator/
├── streamlit_app/
│   └── app.py                      # Streamlit frontend
├── agents/
│   ├── supervisor.py               # Agent router
│   ├── coder.py                    # Code-related logic
│   ├── researcher.py               # Wikipedia + vector research
│   ├── summarizer.py               # Text summarization
│   ├── planner.py                  # Task planning agent
│   └── qa.py                       # General Q&A fallback
├── tools/
│   ├── calculator_tool.py
│   ├── summarizer_tool.py
│   ├── wikipedia_tool.py
│   └── rag_vector_tool.py         # Vector DB + CSV loader
├── vector_store/
│   └── faiss_index/               # Auto-generated FAISS index
├── data/
│   └── knowledge_base.csv         # Pre-filled KB for vector search
├── requirements.txt
├── .env                           # Add your OpenAI API key here
└── README.md
```

---

## 🧪 Example Agent Prompts

| Agent         | Prompt Example                                | Sample Output Snippet                                                   |
| ------------- | --------------------------------------------- | ----------------------------------------------------------------------- |
| 🧠 Supervisor | "Summarize this paragraph for a report"       | Routes to summarizer → returns condensed version                        |
| 🧪 Researcher | "Tell me about Alan Turing"                   | Uses Wikipedia + KB → "Alan Turing was a British computer scientist..." |
| 🧮 Calculator | "What is (20 + 5) \* 2?"                      | → "The result is 50."                                                   |
| 📃 Summarizer | "Summarize: The Industrial Revolution..."     | → "The Industrial Revolution was a period of major change..."           |
| 👨‍💻 Coder   | "Write Python code to sort a list of numbers" | → "Here's how to do it using `sorted(numbers)`..."                      |
| 📅 Planner    | "Plan a product launch campaign in 5 steps"   | → "1. Research market, 2. Define goals, ..."                            |
| 📚 Retriever  | "What is unsupervised learning?"                     | → "Acme Corp specializes in supply chain analytics..."                  |

---

## ⚙️ How to Run

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/amitkharche/agentic-ai-orchestrator.git
cd agentic-ai-orchestrator
```

---

### ✅ 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ✅ 3. Configure OpenAI API

Create a `.env` file:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Alternatively, you'll be prompted to enter it on app startup.

---

### ✅ 4. Launch the Streamlit UI

```bash
streamlit run streamlit_app/app.py
```

What happens:

* ✅ Loads the FAISS vector DB from `knowledge_base.csv`
* ✅ Registers all agents and tools with LangGraph
* ✅ UI opens for live prompt interaction

---

## 🔍 How RAG (Vector Search) Works

1. **knowledge\_base.csv** is split into chunks
2. Each chunk is embedded using OpenAI embeddings
3. Vector DB is created with FAISS and stored in `vector_store/`
4. On query, user input is embedded → matched against vector DB
5. Matching entries are fed into the agent for response grounding

✅ Ensures more **accurate**, **fact-based** responses.

---

## 👨‍💻 Example Usage

| Task Type     | What to Ask                                               |
| ------------- | --------------------------------------------------------- |
| Coding        | "Write a Python function to check for prime numbers"      |
| Research      | "What is LangChain used for?"                             |
| Summarization | "Summarize: Large Language Models are neural networks..." |
| Planning      | "Plan a hiring process for a data science team"           |
| KB Search     | "What does XYZ Inc do?"                                   |
| Math          | "What’s 56 \* 3 + 10?"                                    |

---

## 📬 Author & Contact

| Platform | Link                                                 |
| -------- | ---------------------------------------------------- |
| GitHub   | [@amitkharche](https://github.com/amitkharche)       |
| LinkedIn | [Amit Kharche](https://linkedin.com/in/amit-kharche) |
| Medium   | [@amitkharche14](https://medium.com/@amitkharche14)  |

---

## 🔮 Future Enhancements

* 🔁 LangGraph step-by-step execution visualizer
* 🤖 OpenAgents integration for dynamic behavior switching
* 📥 PDF, DOCX, and webpage ingestion for RAG
* 📊 Trulens or LangSmith for LLM observability
* 🧠 Multi-modal agent support (vision + text)

---

# 🧠 Agentic AI Orchestrator with LangChain & Tool Calling

## 📌 Business Use Case

This project simulates a real-world **Agentic AI system** where tasks are routed by a **Supervisor Agent** to appropriate specialized agents:

- 💻 `Coder Agent` – generates code using OpenAI
- 🔍 `Researcher Agent` – performs research using Wikipedia API

It supports:
- ✅ Tool calling (Wikipedia)
- ✅ Memory chaining via LangChain
- ✅ OpenAI API usage with dynamic key handling
- ✅ Streamlit UI

---

## 🧠 Features

- **Streamlit UI** for user-friendly interactions
- **LangChain Agents** with real tools and memory
- **Supervisor Routing** based on task type
- **OpenAI API Key Entry** via `.env` or Streamlit input

---

## 🛠️ Technologies Used

| Component       | Technology         |
|----------------|--------------------|
| UI             | Streamlit          |
| LLM            | OpenAI GPT (via LangChain) |
| Tools          | Wikipedia API      |
| Memory         | LangChain Buffer Memory |
| Agent Logic    | LangChain + Python |
| Secrets        | .env or Streamlit  |

---

## 🧾 Project Structure

```
agentic_ai_tool_memory_app/
├── agents/
│   ├── coder.py              # Coder Agent logic
│   ├── researcher.py         # Researcher Agent logic
│   └── supervisor.py         # Routes tasks
├── streamlit_app/
│   └── app.py                # Streamlit UI
├── .gitignore
├── .env                      # (Optional) OpenAI API Key
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run (Windows Compatible)

```bash
# Step 1: Unzip the project
cd agentic_ai_tool_memory_app

# Step 2: Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the app
streamlit run streamlit_app/app.py
```

> 🔐 You can enter your OpenAI API key in two ways:
> - Add `OPENAI_API_KEY=sk-...` in `.env`
> - Or, enter manually in the Streamlit interface

---

## 💼 Contact

- 🌐 [LinkedIn](https://www.linkedin.com/in/amit-kharche)
- 💻 [GitHub](https://github.com/amitkharche)
- ✍️ [Medium](https://medium.com/@amitkharche14)

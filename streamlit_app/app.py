import os
import sys

# ✅ Add project root to Python path so we can import agents and tools
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Import Streamlit and necessary modules
import streamlit as st
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Verify API key is loaded before importing GPT-dependent modules
if not os.getenv("OPENAI_API_KEY"):
    st.warning("🔐 Please enter your OpenAI API Key to proceed.")
    api_key = st.text_input("Enter OpenAI API Key:", type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
else:
    api_key = os.getenv("OPENAI_API_KEY")

# ✅ Proceed only if key is available
if api_key:
    from agents.supervisor import supervisor_route
    from tools.rag_vector_tool import RAGVectorTool  # Optional use within agents/tools

    st.set_page_config(page_title='🧠 Agentic AI Orchestrator', layout='wide')
    st.title('🧠 Multi-Agent Tool-Calling AI System')

    # ✅ Streamlit input and agent dispatch
    user_input = st.text_area('Enter your task:')
    if st.button('Run Agent'):
        with st.spinner('Thinking...'):
            output = supervisor_route(user_input)
        st.success('Done!')
        st.markdown('### 🧾 Output')
        st.write(output)

else:
    st.stop()

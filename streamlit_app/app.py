import streamlit as st
from agents.supervisor import supervisor_route
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title='🧠 Agentic AI Orchestrator', layout='wide')
st.title('🧠 Multi-Agent Tool-Calling AI System')

user_input = st.text_area('Enter your task:')
if st.button('Run Agent'):
    with st.spinner('Thinking...'):
        output = supervisor_route(user_input)
        st.success('Done!')
        st.markdown('### 🧾 Output')
        st.write(output)

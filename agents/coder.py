from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key='chat_history')

def coder_agent_executor():
    tools = []  # You can add tools like Python REPL
    return initialize_agent(
        tools, llm, agent='chat-conversational-react-description', verbose=True, memory=memory
    )

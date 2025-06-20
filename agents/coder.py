from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory

# Initialize LLM
llm = ChatOpenAI(temperature=0)

# ✅ Ensure memory returns BaseMessage objects (avoids chat_history error)
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

# Coder agent (currently without additional tools)
def coder_agent_executor():
    return initialize_agent(
        tools=[], 
        llm=llm, 
        agent='chat-conversational-react-description', 
        verbose=True, 
        memory=memory
    )

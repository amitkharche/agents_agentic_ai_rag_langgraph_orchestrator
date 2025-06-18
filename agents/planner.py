from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent

# Initialize LLM
llm = ChatOpenAI(temperature=0)

# ✅ Fix: Ensure memory returns a list of BaseMessage objects
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

# Planner agent (no tools for now)
def planner_agent_executor():
    return initialize_agent(
        tools=[], 
        llm=llm, 
        agent='chat-conversational-react-description', 
        verbose=True, 
        memory=memory
    )

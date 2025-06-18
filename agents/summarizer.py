from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from tools.summarizer_tool import summarizer_tool

llm = ChatOpenAI(temperature=0)

# ✅ FIXED: return_messages must be True for chat agents
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

def summarizer_agent_executor():
    return initialize_agent(
        tools=[summarizer_tool],
        llm=llm,
        agent='chat-conversational-react-description',
        verbose=True,
        memory=memory
    )

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from tools.wikipedia_tool import wikipedia_tool
from tools.rag_vector_tool import rag_tool  # ✅ Ensure rag_tool is defined in rag_vector_tool.py

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def researcher_agent_executor():
    return initialize_agent(
        tools=[wikipedia_tool, rag_tool],
        llm=llm,
        agent="chat-conversational-react-description",
        verbose=True,
        memory=memory
    )

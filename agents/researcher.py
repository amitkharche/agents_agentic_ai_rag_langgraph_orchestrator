from langchain.chat_models import ChatOpenAI
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(temperature=0)
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
memory = ConversationBufferMemory(memory_key='chat_history')

def researcher_agent_executor():
    tools = [Tool(name='Wikipedia', func=wiki.run, description='Wikipedia-based research tool')]
    return initialize_agent(
        tools, llm, agent='chat-conversational-react-description', verbose=True, memory=memory
    )

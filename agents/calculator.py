from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
#from langchain.tools.python.tool import PythonREPLTool  # ✅ Correct import
from langchain_experimental.tools import PythonREPLTool

# Then use it as:
python_repl = PythonREPLTool()

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key='chat_history')

def calculator_agent_executor():
    return initialize_agent(
        tools=[PythonREPLTool()],
        llm=llm,
        agent='chat-conversational-react-description',
        verbose=True,
        memory=memory
    )

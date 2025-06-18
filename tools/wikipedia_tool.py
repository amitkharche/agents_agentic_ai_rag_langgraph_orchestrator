from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain.agents import Tool

wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

wikipedia_tool = Tool(
    name="Wikipedia Search",
    func=wiki.run,
    description="Search Wikipedia for general knowledge."
)
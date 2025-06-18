from langchain.agents import Tool

def summarize_text(text):
    return f"Summary: {text[:100]}..."

summarizer_tool = Tool(
    name="Text Summarizer",
    func=summarize_text,
    description="Summarizes long text inputs."
)
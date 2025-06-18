from langchain.tools import Tool

def simple_calculator(query: str) -> str:
    try:
        return str(eval(query))
    except Exception as e:
        return f"❌ Error in calculation: {e}"

calculator_tool = Tool(
    name="Calculator",
    func=simple_calculator,
    description="Use this tool for arithmetic questions like 'What is (20 + 5) * 2?'"
)

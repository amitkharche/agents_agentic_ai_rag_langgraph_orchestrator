from agents.researcher import researcher_agent_executor
from agents.coder import coder_agent_executor
from agents.planner import planner_agent_executor
from agents.summarizer import summarizer_agent_executor
from agents.calculator import calculator_agent_executor  # ✅ Add this

def supervisor_route(task: str):
    if not task:
        return "⚠️ Please enter a valid task."

    task_lower = task.lower().strip()
    print(f"[Supervisor] Received Task: {task_lower}")

    if any(kw in task_lower for kw in ["code", "python", "function", "script", "program"]):
        return coder_agent_executor().run(task)

    elif any(kw in task_lower for kw in ["research", "explain", "who is", "what is", "tell me", "history", "facts"]):
        return researcher_agent_executor().run(task)

    elif any(kw in task_lower for kw in ["plan", "steps", "strategy", "roadmap", "timeline", "launch"]):
        return planner_agent_executor().run(task)

    elif any(kw in task_lower for kw in ["summarize", "summary", "shorten", "sumarize"]):
        return summarizer_agent_executor().run(task)

    elif any(kw in task_lower for kw in ["calculate", "+", "-", "*", "/", "math", "what is", "how much"]):
        return calculator_agent_executor().run(task)

    else:
        return "🤖 Supervisor: Unrecognized task. Try with keywords like: code, research, plan, summarize, calculate."

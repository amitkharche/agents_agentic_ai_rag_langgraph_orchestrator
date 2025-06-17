from agents.researcher import researcher_agent_executor
from agents.coder import coder_agent_executor

def supervisor_route(task):
    if 'code' in task.lower():
        return coder_agent_executor().run(task)
    elif 'research' in task.lower() or 'explain' in task.lower():
        return researcher_agent_executor().run(task)
    else:
        return '🤖 Supervisor: Unrecognized task. Try with code or research prompt.'

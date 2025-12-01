# uniassist_ai/agents/unified_agent.py
from uniassist_ai.gemini_client import ask_gemini

class UnifiedAgent:
    """
    Example unified agent that can call internal tools + Gemini.
    Use methods from tools/* when implemented.
    """
    def __init__(self):
        pass

    def handle(self, query: str) -> str:
        # A single prompt can request multiple outputs
        prompt = (
            f"You are the UniAssist unified agent. The user said: {query}\n"
            "Decide whether to: plan meal, schedule workout, make shopping list or plan travel. "
            "If multiple tasks are asked, separate results with '---'."
        )
        return ask_gemini(prompt, temperature=0.2, max_output_tokens=900)

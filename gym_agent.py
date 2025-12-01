from uniassist_ai.gemini_client import ask_gemini

class GymAgent:
    def handle(self, query: str):
        prompt = f"Create a complete workout or fat-loss fitness plan for: {query}"
        return ask_gemini(prompt)

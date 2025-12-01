from uniassist_ai.gemini_client import ask_gemini

class GymAgent:
    def handle(self, query: str):
        prompt = f"Create a workout, fat loss plan and fitness guidance for: {query}"
        return ask_gemini(prompt)

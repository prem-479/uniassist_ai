from uniassist_ai.gemini_client import ask_gemini

class MealAgent:
    def handle(self, query: str):
        prompt = f"Create a healthy and affordable meal plan for: {query}"
        return ask_gemini(prompt)

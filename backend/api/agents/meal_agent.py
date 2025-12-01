from api.gemini_client import ask_gemini

class MealAgent:
    def handle(self, message):
        prompt = f"You are a meal planning AI. User said: {message}"
        return ask_gemini(prompt)

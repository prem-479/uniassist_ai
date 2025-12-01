from api.gemini_client import ask_gemini

class GymAgent:
    def handle(self, message):
        prompt = f"You are a fitness & workout assistant. User said: {message}"
        return ask_gemini(prompt)

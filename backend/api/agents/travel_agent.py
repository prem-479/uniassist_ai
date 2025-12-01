from api.gemini_client import ask_gemini

class TravelAgent:
    def handle(self, message):
        prompt = f"You are a travel planning assistant. User said: {message}"
        return ask_gemini(prompt)

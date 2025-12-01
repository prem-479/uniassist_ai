from api.gemini_client import ask_gemini

class ShoppingAgent:
    def handle(self, message):
        prompt = f"You are a shopping/product recommendation assistant. User said: {message}"
        return ask_gemini(prompt)

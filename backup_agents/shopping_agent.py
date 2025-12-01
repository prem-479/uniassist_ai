from uniassist_ai.gemini_client import ask_gemini

class ShoppingAgent:
    def handle(self, query: str):
        prompt = f"Generate a detailed shopping list with best prices for: {query}"
        return ask_gemini(prompt)

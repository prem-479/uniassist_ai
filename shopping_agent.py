from uniassist_ai.gemini_client import ask_gemini

class ShoppingAgent:
    def handle(self, query: str):
        prompt = f"Create a shopping list with cheapest stores for: {query}"
        return ask_gemini(prompt)

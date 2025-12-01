from uniassist_ai.gemini_client import ask_gemini

class TravelAgent:
    def handle(self, query: str):
        prompt = f"Create a smart travel plan, flight suggestions and itinerary for: {query}"
        return ask_gemini(prompt)

from uniassist_ai.gemini_client import ask_gemini

class TravelAgent:
    def handle(self, query: str):
        prompt = f"Give a full travel plan (flight + hotel + itinerary) for: {query}"
        return ask_gemini(prompt)

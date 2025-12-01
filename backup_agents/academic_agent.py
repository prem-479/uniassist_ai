from uniassist_ai.gemini_client import ask_gemini

class AcademicAgent:
    def handle(self, query: str):
        prompt = f"Provide academic help, ML interview prep or study guidance for: {query}"
        return ask_gemini(prompt)

from uniassist_ai.gemini_client import ask_gemini

class AcademicAgent:
    def handle(self, query: str):
        prompt = f"Give academic help, study guidance or interview preparation for: {query}"
        return ask_gemini(prompt)

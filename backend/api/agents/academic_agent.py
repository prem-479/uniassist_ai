from api.gemini_client import ask_gemini

class AcademicAgent:
    def handle(self, message):
        prompt = f"You are a study/academic assistant. User said: {message}"
        return ask_gemini(prompt)

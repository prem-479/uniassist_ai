import os
import google.generativeai as genai

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is missing.")

genai.configure(api_key=API_KEY)

# Correct model name
MODEL = "models/gemini-1.5-flash"


def ask_gemini(prompt: str):
    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[Gemini Error] {str(e)}"

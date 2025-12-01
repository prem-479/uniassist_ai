import google.generativeai as genai
import os

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise Exception("❌ GEMINI_API_KEY not found. Set it in environment variables.")

genai.configure(api_key=API_KEY)
MODEL_NAME = "models/gemini-2.5-flash"

def ask_gemini(text):
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        return f"[Gemini Error] {e}"

def classify_intent(text):
    prompt = f"""
Classify this user request into ONE category only:
meal, gym, shopping, travel, academic, unknown.

User request: {text}

Return just one word.
"""
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text.strip().lower()
    except:
        return "unknown"

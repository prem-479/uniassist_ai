import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.0-flash")

resp = model.generate_content("Hello! Reply OK if this is working.")

print("Gemini response:", resp.text)

# ai_generator.py

import google.generativeai as genai

# Set your Gemini API key
API_KEY = "AIzaSyDRWRMg3Ui3oJX_mB4O10HL0ZDHYS3rZ_M"

genai.configure(api_key=API_KEY)

# Load the Gemini 2.0 Flash model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import re

# Load API key
load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

# Choose model
model = genai.GenerativeModel("gemini-1.5-flash")

# FastAPI app
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Health check
@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        user_message = data.get("message", "")
        print("📨 USER:", user_message)



        prompt = f"""You are a helpful AI assistant named SleepTracker AI. 
You ONLY talk about topics related to sleep quality, sleep hygiene, or sleep-affecting habits.

❌ If a user asks anything outside the topic of sleep, respond:
"Buddy! I'm here to help with your sleep.  Share more about your sleep patterns, habits, or concerns?"

✅ Regardless of the user input, ALWAYS respond with a JSON like this:

{{
  "response": "Your reply here",
  "factors": {{
    "caffeine": number between 0-100,
    "screen_time": number between 0-100,
    "stress": number between 0-100
  }}
}}

Even if the input is unrelated, the 'factors' must still be returned with default 0 values.

User message: \"{user_message}\"
"""


        gemini_response = model.generate_content(prompt)
        print("🧠 GEMINI RAW:", gemini_response.text)

        # --- Fix begins here ---
        clean_text = re.sub(r"^```json|```$", "", gemini_response.text.strip()).strip()
        response_dict = json.loads(clean_text)
        return response_dict

    except Exception as e:
        print("❌ BACKEND ERROR:", e)
        return {"error": "Error processing your message."}

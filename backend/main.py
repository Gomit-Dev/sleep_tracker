from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

# Configure your Gemini API key hereimport os
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-pro")

# Setup FastAPI app
app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend domain if deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for chat input
class ChatInput(BaseModel):
    message: str

# POST route to handle chat
@app.post("/chat")
async def chat_with_bot(data: ChatInput):
    try:
        prompt = f"You are SleepTracker AI, a friendly sleep assistant helping users with sleep advice, tips, and schedules.\nUser: {data.message}\nAI:"
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}

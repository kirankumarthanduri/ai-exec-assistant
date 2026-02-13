from google import genai
from config import GEMINI_API_KEY

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
You are an executive assistant.

Your job is to summarize emails and calendar events clearly and concisely.
Always extract:
- Key points
- Action items
- Deadlines
- Priority (High / Medium / Low)

Be brief, professional, and structured.
"""

def summarize(text: str) -> str:
    response = client.models.generate_content(
        model="gemini-1.5-pro",   # This now works
        contents=f"{SYSTEM_PROMPT}\n\nUser Input:\n{text}",
        config={
            "temperature": 0.3
        }
    )

    return response.text.strip()

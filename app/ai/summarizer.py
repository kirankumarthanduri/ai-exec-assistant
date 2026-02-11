from openai import OpenAI
from config import OPENAI_API_KEY

# Create OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# System prompt (MUST be defined)
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
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()

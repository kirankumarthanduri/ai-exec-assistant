import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Debug print (temporary)
print("DEBUG config.py -> GEMINI_API_KEY  exists:", GEMINI_API_KEY  is not None)

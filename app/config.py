import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Debug print (temporary)
print("DEBUG config.py -> OPENAI_API_KEY exists:", OPENAI_API_KEY is not None)

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Google API key
genai.configure(api_key=api_key)

# Use the Gemini 2.0 Flash model
model = genai.GenerativeModel(model_name="gemini-2.0-flash-001")

# Send a simple prompt
response = model.generate_content("Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")

# Print the response text
print(response.text)
usage = response.usage_metadata
print(f"Prompt tokens: {usage.prompt_token_count}")
print(f"Response tokens: {usage.candidates_token_count}")
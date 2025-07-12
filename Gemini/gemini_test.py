import google.generativeai as genai
import os 
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Define the prompt
prompt = "Tell me a fun fact about the solar system."

# 4. Generate content
try:
    response = model.generate_content(prompt)
    
    # 5. Print the generated text
    print("Generated Response:")
    print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure your API key is correct and you have network connectivity.")
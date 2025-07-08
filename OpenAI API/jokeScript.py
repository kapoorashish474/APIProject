
import openai
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)
def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        print(response.choices[0].message.content)
    except openai.RateLimitError as e:
        error_message = e.response.json()["error"]["message"]
        error_code = e.response.status_code
        return f"Error {error_code}: {error_message}"

user_prompt = "Tell me a joke"
print(chat_with_gpt(user_prompt))

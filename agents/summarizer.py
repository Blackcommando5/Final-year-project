from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize(text: str):
    if not text.strip():
        return "No text provided for summarization."
    
    try:
        # Replace with a valid model from your account
        result = client.models.generate_content(
            model="gemini-2.5-flash",  
            contents=[{
                "role": "user",
                "parts": [{"text": f"Summarize this meeting:\n{text}"}]
            }],
        )
        return result.candidates[0].content.parts[0].text
    except Exception as e:
        return f"Error while summarizing: {str(e)}"

# Only list models when running this file directly
if __name__ == "__main__":
    models = client.models.list()
    for m in models:
        print(m.name)

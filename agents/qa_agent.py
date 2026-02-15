from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def answer_question(question: str, context: str):
    result = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[{"role": "user", "parts": [{"text": f"Context:\n{context}\n\nQuestion:\n{question}"}]}],
    )
    return result.candidates[0].content.parts[0].text

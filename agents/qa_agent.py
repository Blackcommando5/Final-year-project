from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def answer_question(question: str, context: str):
    prompt = f"""
You are a meeting assistant. Answer ONLY using the transcript below.
If the answer is not clearly present in the transcript, reply exactly:
"Not mentioned in the transcript."

Transcript:
{context}

Question:
{question}

Answer (short and direct):
"""
    result = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[{"role": "user", "parts": [{"text": prompt}]}],
    )
    return result.candidates[0].content.parts[0].text.strip()
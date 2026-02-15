from dotenv import load_dotenv
load_dotenv()   # 👈 THIS FIXES YOUR ERROR

from fastapi import FastAPI
from pydantic import BaseModel
from agents.orchestrator import Orchestrator

app = FastAPI()
agent = Orchestrator()

class TranscriptIn(BaseModel):
    text: str

class QuestionIn(BaseModel):
    question: str

@app.post("/transcript")
def send_transcript(data: TranscriptIn):
    agent.add_transcript(data.text)
    return {"status": "ok"}

@app.get("/summary")
def get_summary():
    return {"summary": agent.run_summary()}

@app.get("/actions")
def get_actions():
    return {"actions": agent.run_actions()}

@app.post("/ask")
def ask_agent(q: QuestionIn):
    return {"answer": agent.run_qa(q.question)}

@app.get("/")
def root():
    return {"message": "Welcome to the Meeting AI backend! Visit /docs for API documentation."}

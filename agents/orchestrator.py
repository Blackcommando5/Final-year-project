from agents.summarizer import summarize
from agents.action_agent import extract_actions
from agents.qa_agent import answer_question

class Orchestrator:
    def __init__(self):
        self.transcript = ""

    def add_transcript(self, text: str):
        self.transcript += "\n" + text

    def run_summary(self):
        if not self.transcript.strip():
            return "No transcript received yet."
        return summarize(self.transcript)

    def run_actions(self):
        if not self.transcript.strip():
            return []
        return extract_actions(self.transcript)

    def run_qa(self, question: str):
        if not self.transcript.strip():
            return "No transcript available."
        return answer_question(question, self.transcript)

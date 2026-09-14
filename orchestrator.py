import sys
from agents.intent_extractor import extract_intent
from agents.gemini_collector import collect
from agents.claude_critic import critique
from agents.final_analyzer import analyze

def run(prompt: str) -> str:
    """Run the full AI Council workflow for a given user prompt."""
    intent = extract_intent(prompt)
    # Use the search_query if provided, otherwise fall back to the full prompt
    query = intent.get('search_query') or prompt
    gemini_output = collect(query)
    refined = critique(gemini_output, intent)
    answer = analyze(intent, refined)
    return answer

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python orchestrator.py \"<prompt>\"")
        sys.exit(1)
    print(run(sys.argv[1]))

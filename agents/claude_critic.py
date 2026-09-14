import os
import json
import anthropic

def critique(gemini_output: dict, intent: dict) -> dict:
    """Critique Gemini's data using Claude.
    Returns a dict with keys: refined_data, critique.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY") or os.getenv("CLAUDE_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY or CLAUDE_API_KEY not set in environment")
    client = anthropic.Anthropic(api_key=api_key)
    prompt = (
        f"You are a data quality reviewer. The user requested: {intent.get('task')}\n"
        f"Original collected data:\n{gemini_output.get('data')}\n\n"
        "Please critique the information for accuracy, completeness, and recency, and provide recommendations or refined points."
    )
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        temperature=0,
        messages=[{"role": "user", "content": prompt}],
    )
    critique_text = "".join(block.text for block in response.content if getattr(block, "type", None) == "text")
    return {"refined_data": gemini_output.get('data'), "critique": critique_text}

if __name__ == "__main__":
    import sys, ast
    gemini_output = ast.literal_eval(sys.argv[1])
    intent = ast.literal_eval(sys.argv[2])
    print(json.dumps(critique(gemini_output, intent)))

import os
import json
import openai

def extract_intent(prompt: str) -> dict:
    """Extract intent from a user prompt using ChatGPT.
    Returns a dict with keys: task, search_query, additional_context.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in environment")
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Extract the user's intent and output a JSON with fields: task, search_query, additional_context."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    content = response.choices[0].message.content.strip()
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {"task": prompt, "search_query": prompt, "additional_context": content}

if __name__ == "__main__":
    import sys
    print(json.dumps(extract_intent(sys.argv[1])))

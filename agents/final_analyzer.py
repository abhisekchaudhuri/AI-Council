import json, openai

def analyze(intent: dict, refined: dict) -> str:
    """Final analysis using ChatGPT.
    Combines intent and refined data, returns a user‑facing answer.
    """
    prompt = (
        f"Task: {intent.get('task')}\n"
        f"Context: {intent.get('additional_context')}\n"
        f"Data: {refined.get('refined_data')}\n"
        "Provide a concise answer addressing the original request."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are an analyst."}, {"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    import sys, ast
    intent = ast.literal_eval(sys.argv[1])
    refined = ast.literal_eval(sys.argv[2])
    print(analyze(intent, refined))

import os
import openai

def analyze(intent: dict, refined: dict) -> str:
    """Final analysis using ChatGPT.
    Combines intent and refined data, returns a user-facing answer.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in environment")
    client = openai.OpenAI(api_key=api_key)
    prompt = (
        f"Task: {intent.get('task')}\n"
        f"Context: {intent.get('additional_context')}\n"
        f"Data: {refined.get('refined_data')}\n"
        f"Critique Insights: {refined.get('critique')}\n"
        "Provide a comprehensive, high-quality answer addressing the original request."
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert analyst synthesizing data into clear, insightful solutions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    import sys, ast
    intent = ast.literal_eval(sys.argv[1])
    refined = ast.literal_eval(sys.argv[2])
    print(analyze(intent, refined))

import os, json
import google.generativeai as genai

def collect(query: str) -> dict:
    """Collect data from Gemini based on a search query.
    Returns a dict with keys: data, source_summary.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set in environment")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        query,
        generation_config={"temperature": 0},
    )
    text = response.text
    return {"data": text, "source_summary": f"Collected using query: {query}"}

if __name__ == "__main__":
    import sys
    print(json.dumps(collect(sys.argv[1])))

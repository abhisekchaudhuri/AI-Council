# AI Council

This repository contains an orchestration workflow that combines three LLM providers:
- **ChatGPT** for intent extraction and final analysis
- **Gemini** for internet search / data acquisition
- **Claude** for data critique and refinement

## Directory Layout
```
ai_council/
├─ agents/
│   ├─ intent_extractor.py
│   ├─ gemini_collector.py
│   ├─ claude_critic.py
│   └─ final_analyzer.py
├─ orchestrator.py
├─ tests/
│   └─ test_ai_council.py
├─ .env.example
├─ pyproject.toml
└─ README.md
```

## Quick Start
1. Copy `.env.example` to `.env` and fill in your API keys.
2. Install dependencies:
   ```bash
   python -m venv venv && source venv/bin/activate
   pip install -r requirements.txt   # or `poetry install`
   ```
3. Run the orchestrator:
   ```bash
   python orchestrator.py "Your prompt here"
   ```
4. Run the test suite:
   ```bash
   pytest -q
   ```

---
*The code files are generated in the `scratch/ai_council/` directory. Adjust the path as needed for your project.*

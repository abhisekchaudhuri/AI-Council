import pytest
from unittest.mock import patch
from orchestrator import run

@pytest.fixture
def sample_prompt():
    return "Give me the latest stats on electric vehicle adoption in Europe."

def test_end_to_end(sample_prompt):
    with patch('agents.intent_extractor.extract_intent') as mock_intent,
         patch('agents.gemini_collector.collect') as mock_collect,
         patch('agents.claude_critic.critique') as mock_critique,
         patch('agents.final_analyzer.analyze') as mock_analyze:
        mock_intent.return_value = {
            "task": "EV adoption stats",
            "search_query": "electric vehicle adoption Europe 2024",
            "additional_context": ""
        }
        mock_collect.return_value = {"data": "raw data", "source_summary": ""}
        mock_critique.return_value = {"refined_data": "clean data", "critique": "All good"}
        mock_analyze.return_value = "Final answer"
        result = run(sample_prompt)
        assert result == "Final answer"
        mock_intent.assert_called_once_with(sample_prompt)
        mock_collect.assert_called_once_with("electric vehicle adoption Europe 2024")
        mock_critique.assert_called_once()
        mock_analyze.assert_called_once()

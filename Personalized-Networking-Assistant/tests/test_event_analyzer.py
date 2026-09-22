# tests/test_event_analyzer.py

from app.services import event_analyzer

def test_event_analysis_returns_labels():
    result = event_analyzer.extract_event_themes("AI in healthcare and diagnostics")
    assert isinstance(result, list)
    assert len(result) > 0
    assert len(result) <= 3
    for label in result:
        assert isinstance(label, str)

# tests/test_topic_generator.py

from app.services import topic_generator

def test_topic_generation_returns_suggestions():
    themes = ["AI", "healthcare"]
    interests = ["ethics", "automation"]
    suggestions = topic_generator.generate_topics(themes, interests)
    assert isinstance(suggestions, list)
    assert len(suggestions) > 0
    assert len(suggestions) <= 3
    for s in suggestions:
        assert isinstance(s, str)
        assert len(s.strip()) > 0

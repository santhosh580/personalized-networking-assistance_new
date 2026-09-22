# tests/test_fact_checker.py

from unittest.mock import patch, MagicMock
from app.services import fact_checker

@patch('app.services.fact_checker.requests.get')
def test_fact_checker_returns_summary(mock_get):
    # Happy path mock
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "extract": "Artificial Intelligence is intelligence demonstrated by machines."
    }
    mock_get.return_value = mock_response

    summary = fact_checker.fact_check("Artificial Intelligence")
    assert isinstance(summary, str)
    assert "intelligence" in summary.lower()

@patch('app.services.fact_checker.requests.get')
def test_fact_checker_missing_data(mock_get):
    # Missing data mock
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    summary = fact_checker.fact_check("UnknownTopic123")
    assert isinstance(summary, str)
    assert "no wikipedia page found" in summary.lower()

@patch('app.services.fact_checker.requests.get')
def test_fact_checker_error_path(mock_get):
    # Error mock
    mock_get.side_effect = Exception("Network timeout")

    summary = fact_checker.fact_check("ErrorQuery")
    assert isinstance(summary, str)
    assert "failed" in summary.lower()

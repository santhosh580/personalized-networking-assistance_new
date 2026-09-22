# app/services/fact_checker.py

import requests
from app.config import FACT_CHECK_API

def fact_check(query: str) -> str:
    try:
        # Format query for Wikipedia page title (replace spaces with underscores)
        formatted_query = query.strip().replace(" ", "_")
        headers = {
            "User-Agent": "PersonalizedNetworkingAssistant/1.0 (jayanthisrikar@gmail.com)"
        }
        response = requests.get(f"{FACT_CHECK_API}/{formatted_query}", headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("extract", "No summary found.")
        elif response.status_code == 404:
            return f"No Wikipedia page found for '{query}'."
        else:
            return f"Fact-checking failed with status code {response.status_code}."
    except Exception as e:
        return f"Fact-checking failed: {str(e)}"

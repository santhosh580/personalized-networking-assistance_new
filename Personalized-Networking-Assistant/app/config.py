# app/config.py

MODEL_NAMES = {
    "event_analysis": "typeform/distilbert-base-uncased-mnli",
    "text_generator": "gpt2"
}

FACT_CHECK_API = "https://en.wikipedia.org/api/rest_v1/page/summary"

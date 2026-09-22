# app/routers/conversation.py

from fastapi import APIRouter
from app.models.schemas import (
    EventInput,
    ConversationRequest,
    FactCheckRequest,
    ConversationResponse,
    FactCheckResponse,
    FeedbackRequest
)
from app.services import event_analyzer, topic_generator, fact_checker, history_logger, feedback_logger

router = APIRouter()

@router.post("/analyze-event")
def analyze_event(data: EventInput):
    themes = event_analyzer.extract_event_themes(data.description)
    return {"topics": themes}

@router.post("/fact-check", response_model=FactCheckResponse)
def fact_check(data: FactCheckRequest):
    summary = fact_checker.fact_check(data.query)
    return FactCheckResponse(summary=summary)

@router.post("/generate-conversation", response_model=ConversationResponse)
def generate_conversation(data: ConversationRequest):
    themes = event_analyzer.extract_event_themes(data.description)
    suggestions = topic_generator.generate_topics(themes, data.interests)
    
    # Save to history
    history_logger.log_conversation({
        "description": data.description,
        "interests": data.interests,
        "topics": themes,
        "suggestions": suggestions
    })
    
    return ConversationResponse(topics=themes, suggestions=suggestions)

@router.post("/feedback")
def submit_feedback(data: FeedbackRequest):
    feedback_logger.log_feedback(data.suggestion, data.feedback)
    return {"status": "success", "message": "Feedback logged successfully."}

@router.get("/history")
def get_history():
    return history_logger.load_history()

@router.get("/feedback")
def get_all_feedback():
    return feedback_logger.get_feedback()

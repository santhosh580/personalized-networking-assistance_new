# app/services/topic_generator.py

from transformers import pipeline, set_seed
from app.config import MODEL_NAMES

generator = pipeline("text-generation", model=MODEL_NAMES["text_generator"])
set_seed(42)

def generate_topics(event_themes, user_interests):
    prompt = (
        f"I'm attending a networking event focused on {', '.join(event_themes)}. "
        f"I'm personally interested in {', '.join(user_interests)}. "
        f"What are three creative and engaging conversation starters I could use to break the ice?"
    )

    outputs = generator(prompt, max_length=150, num_return_sequences=1)
    # Post-process to extract suggestions
    generated_text = outputs[0]["generated_text"]
    
    # We remove the prompt from the generated text if the model outputs it
    if generated_text.startswith(prompt):
        generated_text = generated_text[len(prompt):]
        
    suggestions = generated_text.split("\n")
    cleaned_suggestions = []
    for s in suggestions:
        s_clean = s.strip("- ").strip("* ").strip().strip("1. ").strip("2. ").strip("3. ")
        if s_clean and len(cleaned_suggestions) < 3:
            cleaned_suggestions.append(s_clean)
            
    # Fallback if no suggestions generated or post-processing didn't find lines
    if not cleaned_suggestions:
        cleaned_suggestions = [
            f"Hi! I saw this event is about {', '.join(event_themes)}. What brings you here?",
            f"Are you also working in {', '.join(user_interests)}? I'd love to chat about that.",
            f"What's your take on the latest trends in {event_themes[0] if event_themes else 'networking'}?"
        ]
    elif len(cleaned_suggestions) < 3:
        cleaned_suggestions.append(f"Are you also working in {', '.join(user_interests)}? I'd love to chat about that.")
        cleaned_suggestions.append(f"What's your take on the latest trends in {event_themes[0] if event_themes else 'networking'}?")
        
    return cleaned_suggestions[:3]

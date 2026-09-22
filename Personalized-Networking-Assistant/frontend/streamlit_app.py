# frontend/streamlit_app.py

import streamlit as st
import requests
import json
from pathlib import Path
import sys

# Backend base URL
BASE_URL = "http://127.0.0.1:8000"

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PREMIUM MODERN CSS STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    .main .block-container {
        font-family: 'Plus Jakarta Sans', sans-serif;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 800 !important;
    }
    
    /* Title Gradient */
    .title-gradient {
        background: linear-gradient(135deg, #3B82F6 0%, #8B5CF6 50%, #EC4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    /* Glassmorphism Cards */
    .feature-card {
        background: rgba(30, 41, 59, 0.45);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(8px);
        transition: all 0.3s ease;
    }
    .feature-card:hover {
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 8px 30px rgba(99, 102, 241, 0.15);
        transform: translateY(-2px);
    }
    
    .starter-text {
        font-size: 1.05rem;
        color: #F8FAFC;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .theme-badge {
        display: inline-block;
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%);
        border: 1px solid rgba(139, 92, 246, 0.3);
        color: #C084FC;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    /* Fact Check Banner */
    .wiki-banner {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(5, 150, 105, 0.08) 100%);
        border: 1px solid rgba(16, 185, 129, 0.25);
        border-radius: 12px;
        padding: 1.25rem;
        color: #E2E8F0;
        margin-top: 1rem;
    }
    
    /* Footer Style */
    .footer-text {
        text-align: center;
        font-size: 0.8rem;
        color: #64748B;
        margin-top: 3rem;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        padding-top: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR DESIGN ---
with st.sidebar:
    st.markdown("### 🤝 Profile & Stats")
    st.info("👋 Welcome to your networking assistant. Configure your profile goals below.")
    
    st.markdown("#### **Active Team Members**")
    st.markdown("""
    - **Jayanthi Srikar** (Lead)
    - **Santhosh Kumar A arugula**
    - **Shubhajit Khanrah**
    - **Rupesh Sairam Reddy K**
    - **Yatham Sridhar Reddy**
    """)
    
    st.markdown("---")
    st.markdown("#### **Project Specifications**")
    st.caption("• Framework: FastAPI & Streamlit")
    st.caption("• Models: DistilBERT & GPT-2")
    st.caption("• Storage: Secure Local Persistence")

# --- MAIN PAGE HEADER ---
st.markdown('<div class="title-gradient">Personalized Networking Assistant</div>', unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.2rem; color: #94A3B8; margin-bottom: 2rem;'>An AI-driven full-stack application that leverages lightweight, secure NLP models to help you engage confidently in social and business environments.</p>", unsafe_allow_html=True)

# --- TAB CONTROL ---
tab1, tab2, tab3 = st.tabs(["🤝 Generate Starters", "🔍 Quick Fact-Check", "🕒 History & Analytics"])

# --- TAB 1: GENERATE STARTERS ---
with tab1:
    col_input, col_output = st.columns([1, 1])
    
    with col_input:
        st.markdown("### 📝 Input Event Context")
        event_description = st.text_area(
            "Enter Event Description", 
            placeholder="Paste speaker outlines, conference topics, or event details here...",
            height=150
        )
        
        user_interests = st.text_input(
            "Your Interests (comma-separated)",
            placeholder="e.g., climate change, urban planning, machine learning"
        )
        
        generate_btn = st.button("✨ Generate Tailored Starters", use_container_width=True)
        
        if generate_btn:
            if event_description and user_interests:
                payload = {
                    "description": event_description,
                    "interests": [i.strip() for i in user_interests.split(",") if i.strip()]
                }
                
                with st.spinner("Processing event context using DistilBERT & GPT-2..."):
                    try:
                        response = requests.post(f"{BASE_URL}/generate-conversation", json=payload)
                        if response.status_code == 200:
                            data = response.json()
                            st.session_state["topics"] = data["topics"]
                            st.session_state["suggestions"] = data["suggestions"]
                            st.toast("Starters generated successfully!", icon="🔥")
                        else:
                            st.error("Failed to generate conversation starters from backend API.")
                    except Exception as e:
                        st.error(f"Could not connect to the backend server: {str(e)}")
            else:
                st.warning("Please fill in both the event description and your interests.")
                
    with col_output:
        st.markdown("### 💡 Tailored Conversation Icebreakers")
        if "suggestions" in st.session_state:
            st.markdown("#### **Extracted Event Themes**")
            badge_html = "".join([f'<span class="theme-badge">🏷️ {topic}</span>' for topic in st.session_state["topics"]])
            st.markdown(badge_html, unsafe_allow_html=True)
            st.markdown("<br/>", unsafe_allow_html=True)
            
            st.markdown("#### **Suggested Openers**")
            for i, suggestion in enumerate(st.session_state["suggestions"]):
                st.markdown(f"""
                <div class="feature-card">
                    <p class="starter-text">💬 "{suggestion}"</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Feedback options in cards
                btn_col1, btn_col2 = st.columns([1, 1])
                with btn_col1:
                    if st.button("👍 Like", key=f"like_{i}"):
                        try:
                            requests.post(f"{BASE_URL}/feedback", json={"suggestion": suggestion, "feedback": "like"})
                            st.toast("Liked!", icon="👍")
                        except Exception as e:
                            st.error(f"Feedback connection failed: {e}")
                with btn_col2:
                    if st.button("👎 Dislike", key=f"dislike_{i}"):
                        try:
                            requests.post(f"{BASE_URL}/feedback", json={"suggestion": suggestion, "feedback": "dislike"})
                            st.toast("Disliked.", icon="👎")
                        except Exception as e:
                            st.error(f"Feedback connection failed: {e}")
        else:
            st.info("Enter details on the left panel and click 'Generate' to display conversational starters.")

# --- TAB 2: QUICK FACT-CHECK ---
with tab2:
    st.markdown("### 🔍 Wikipedia Fact-Checking Assistant")
    st.markdown("<p style='color: #94A3B8;'>Quickly query Wikipedia summary REST APIs to build background knowledge on unfamiliar topics or buzzwords prior to your discussion.</p>", unsafe_allow_html=True)
    
    query = st.text_input(
        "Enter a topic or buzzword to fact-check",
        placeholder="e.g., Transformer, Blockchain, Smart Grid"
    )
    
    check_btn = st.button("Verify Term", use_container_width=True)
    
    if check_btn:
        if query:
            with st.spinner(f"Retrieving definition for '{query}'..."):
                try:
                    response = requests.post(f"{BASE_URL}/fact-check", json={"query": query})
                    if response.status_code == 200:
                        summary = response.json()["summary"]
                        st.markdown(f"""
                        <div class="wiki-banner">
                            <h4>📘 Wikipedia Reference Check for "{query}"</h4>
                            <p style="font-size: 1rem; line-height: 1.6; margin-top: 0.5rem;">{summary}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.error("Fact-checking request failed.")
                except Exception as e:
                    st.error(f"Could not connect to the backend server: {str(e)}")
        else:
            st.warning("Please enter a keyword to fact-check.")

# --- TAB 3: HISTORY & ANALYTICS ---
with tab3:
    col_hist, col_feed = st.columns([1, 1])
    
    with col_hist:
        st.markdown("### 🕒 Recent Conversation Logs")
        refresh_history = st.button("🔄 Refresh History Logs")
        
        if refresh_history or "history_data" not in st.session_state:
            try:
                r = requests.get(f"{BASE_URL}/history")
                if r.status_code == 200:
                    st.session_state["history_data"] = r.json()
                else:
                    st.session_state["history_data"] = []
            except Exception as e:
                st.error("Could not fetch history from API backend.")
                st.session_state["history_data"] = []
                
        history = st.session_state.get("history_data", [])
        if history:
            for item in reversed(history[-5:]):  # show latest 5
                st.markdown(f"""
                <div class="feature-card">
                    <h5>🕒 {item.get('timestamp', '')}</h5>
                    <p style="margin-top: 0.5rem;"><b>Event Context:</b> {item.get('description', '')}</p>
                    <p><b>Interests:</b> {', '.join(item.get('interests', []))}</p>
                    <p><b>Extracted Topics:</b> {', '.join(item.get('topics', []))}</p>
                    <p><b>Generated Icebreakers:</b></p>
                    <ul>
                        {''.join([f'<li>"{s}"</li>' for s in item.get('suggestions', [])])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No past logs found. Generate some starters to create history logs!")
            
    with col_feed:
        st.markdown("### 📊 Thumbs Up / Down Auditing")
        refresh_feedback = st.button("🔄 Refresh Feedback Audit")
        
        if refresh_feedback or "feedback_history" not in st.session_state:
            try:
                r = requests.get(f"{BASE_URL}/feedback")
                if r.status_code == 200:
                    st.session_state["feedback_history"] = r.json()
                else:
                    st.session_state["feedback_history"] = []
            except Exception as e:
                st.error("Could not fetch feedback history from API backend.")
                st.session_state["feedback_history"] = []
                
        feedback_data = st.session_state.get("feedback_history", [])
        if feedback_data:
            for item in reversed(feedback_data[-10:]):  # show latest 10
                icon = "👍 Liked" if item.get("feedback") == "like" else "👎 Disliked"
                color = "#10B981" if item.get("feedback") == "like" else "#EF4444"
                st.markdown(f"""
                <div class="feature-card" style="border-left: 4px solid {color};">
                    <p style="font-weight: 600; color: {color}; margin: 0;">{icon}</p>
                    <p style="margin-top: 0.5rem; font-style: italic;">"{item.get('suggestion', '')}"</p>
                    <caption style="font-size: 0.75rem; color: #64748B;">Logged at: {item.get('timestamp', '')}</caption>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No user ratings logged yet.")

# --- FOOTER ---
st.markdown('<div class="footer-text">Personalized Networking Assistant | AI-ML & GenAI Track Project Submission</div>', unsafe_allow_html=True)

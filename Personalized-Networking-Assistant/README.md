# Personalized Networking Assistant

An AI-powered web application that helps users generate smart, tailored conversation starters for professional or social networking events. 

Built using **FastAPI** for a modular, high-performance backend and **Streamlit** for an interactive, responsive frontend.

---

## 🚀 Key Features

* **Event Theme Analyzer (DistilBERT)**: Extracts top categories/themes from event descriptions using zero-shot classification.
* **Tailored Prompt Generator (GPT-2)**: Generates 3 creative conversation starters mapped to the extracted event themes and the user's interests.
* **Wikipedia Fact-Checking**: Integrated search query validation leveraging Wikipedia REST APIs to quickly check buzzwords in real-time.
* **Local Persistence (History & Feedback)**: Saves previous sessions in `history.json` and records user thumbs-up/down ratings in `feedback.json`.

---

## 🛠️ Technology Stack

* **Frontend**: Streamlit
* **Backend**: FastAPI, Uvicorn
* **NLP Models**: HuggingFace Transformers (DistilBERT & GPT-2 Small)
* **API Integration**: Wikipedia summary API
* **Testing**: PyTest, HTTPX TestClient

---

## 📁 Repository Structure

* `/1. Brainstorming & Ideation` - Brainstorming lists, Empathy Map, and Problem Statement PDFs.
* `/2. Requirement Analysis` - Customer Journey, DFD diagram, Requirements, and Tech Stack PDFs.
* `/3. Project Design Phase` - Proposed Solution, Solution Architecture diagram, and Fit Canvas PDFs.
* `/4. Project Planning Phase` - Sprints timeline and backlog estimation PDF.
* `/5. Project Development Phase` - Code checklists, reusability logs, and functional features PDFs.
* `/6.Project Testing` - Performance testing reports PDF.
* `/7.Project Documentation` - Executable files guide and user documentation manual PDFs.
* `/8.Project Demonstration` - Communication logs, Demo planning, Scalability, and Team involvement PDFs.
* `/app` - Core backend FastAPI package (schemas, services, routers, configurations).
* `/frontend` - Interactive Streamlit frontend UI app.
* `/tests` - PyTest automated unit and integration tests.

---

## 💻 Setup and Run Instructions

### Prerequisites
* Python 3.11+
* Git

### Step 1: Clone and Navigate
```bash

```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run FastAPI Backend
```bash
uvicorn app.main:app --port 8000
```
The interactive API Swagger docs will be available at `http://127.0.0.1:8000/docs`.

### Step 4: Run Streamlit Frontend
In a new terminal window, run:
```bash
streamlit run frontend/streamlit_app.py
```
The frontend UI dashboard will be available at `http://localhost:8501`.

---

## 🧪 Running Tests
To run the automated PyTest suite:
```bash
python -m pytest
```

---

## 👥 Team Members

* **Jayanthi Srikar** (Team Lead) - `jayanthisrikar@gmail.com`
* **Santhosh Kumar Arugula** (Member) - `23p31a0580@acet.ac.in`
* **Shubhajit Khanrah** (Member) - `khanrahshubhajit@gmail.com`
* **Rupesh Sairam Reddy Karri** (Member) - `riskerrupesh8@gmail.com`
* **Yatham Sridhar Reddy** (Member) - `yathamsridharreddy99@gmail.com`

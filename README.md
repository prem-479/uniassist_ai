UniAssist AI — Multi-Agent Student Lifestyle Concierge

A powerful multi-agent system designed for ML & engineering students in India.
UniAssist AI automates 12+ hours/week of manual planning across academics, internships, gym & health, meals, shopping, travel, and reminders.

Built with a modular, extensible agent ecosystem inspired by Google ADK patterns.

🚀 Key Capabilities
✓ Meal Planning

Vegetarian + high-protein plans under student budget (₹1500/week) with grocery mapping.

✓ Gym & Health Automation

Workout scheduling, basketball sessions, calorie tracking, rest-day planning.

✓ Academic Assistant

Finds EEG/CV datasets, hackathon deadlines, coursework planner.

✓ Internship & Job Hunter

Scrapes opportunities (mock API), creates tailored resumes, tracks application status.

✓ Travel Planner

Flight & hotel search (mock APIs), internship travel, budget optimization.

✓ Reminders & Calendar Automation

Schedules coursework, workouts, meals, deadlines, interviews.

✓ Dashboard Generator

Creates weekly PDF plan + Gradio interactive dashboard.

🧠 Architecture Overview

UniAssist AI uses 9 specialized LLM-powered agents coordinated via a central router:

        ┌────────────────┐
        │ User Query     │
        └──────┬─────────┘
               ▼
       ┌──────────────┐
       │ Router Agent  │
       └──────┬────────┘
   ┌──────────┴──────────┐
   ▼                     ▼
Parallel Layer 1     Parallel Layer 2
(Meal, Gym,          (Academic,
Shopping)             Job Hunter)
   └──────────┬──────────────┘
              ▼
        Travel Agent
              ▼
      Reminder Agent
              ▼
      Dashboard Agent
              ▼
       Final Outputs
 (PDF + Calendar + UI)

📁 Repository Structure
uniassist_ai/
├── agents/              # All agent classes
├── tools/               # Tool wrappers (Nutrition, BigBasket, LinkedIn, Kaggle, etc.)
├── orchestrator/        # Multi-agent orchestration pipeline
├── memory/              # MemoryBank + sessions
├── evaluation/          # Metrics + A2A tests
├── demo/                # Gradio UI + PDF generator
├── data/                # Sample user profile
├── tests/               # Unit testing suite
├── notebook/            # Colab/Kaggle demo notebook
├── README.md
├── requirements.txt
└── LICENSE

⚙️ Installation
Clone repo
git clone https://github.com/prem-479/uniassist_ai.git
cd uniassist_ai

Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

Install dependencies
pip install -r requirements.txt

▶️ Running the Project
Start the orchestrator
python orchestrator/pipeline.py --demo

Launch Gradio dashboard
python demo/gradio_app.py


Then open:
👉 http://localhost:7860/

🛠️ Tech Stack

Python

Custom Multi-Agent Orchestration

Gradio

FastAPI (for future API mode)

Mock APIs (Nutrition, BigBasket, Kaggle, LinkedIn, Flights)

PDF generation utilities

Memory & session services

📊 Evaluation & Metrics

Included components:

A2A evaluation test harness

Agent latency logging

Task success scoring

Budget constraints validation

Academic deadline adherence metrics

🤖 Why UniAssist AI Stands Out

Fully modular 9-agent architecture

Indian student–specific features (meals, travel, budgets)

Multi-parallel + sequential agent flow

Professional PDF & dashboard outputs

Demonstrates 6+ Kaggle Capstone Requirements:

Multi-agent system

Tools (custom + mock + wrappers)

Memory & sessions

Observability

Evaluation

Long-running tasks

📄 License

Released under the MIT License — free to use and modify.

👤 Author

Prem Mali (prem-479)
GitHub: https://github.com/prem-479/uniassist_ai
1. Problem Statement

Problem:
Creating personalized fitness plans requires expertise across multiple domains—health assessment, nutrition science, exercise programming, and motivational psychology. Most fitness apps provide generic recommendations that do not account for individual needs, goals, or circumstances.

Why Multi-Agent AI:
This problem naturally decomposes into specialized domains where different agents can leverage domain-specific knowledge. Multi-agent collaboration allows each agent to focus on its expertise while the orchestrator ensures a cohesive, integrated plan—mimicking how a real fitness team (nutritionist, trainer, health assessor, motivational coach) would collaborate.

Unique Value of Multi-Agent Collaboration:

The Assessment Agent evaluates user profile and informs other agents.

Nutrition and Exercise Agents generate meal and workout plans based on assessment results.

Motivation Agent encourages adherence and engagement.

The Orchestrator Agent coordinates all outputs, ensuring the final plan is complete, consistent, and personalized.

2. Project Description

Application:
A personalized fitness coaching system that leverages four specialized AI agents coordinated by an orchestrator:

Assessment Agent: Analyzes user profile (age, weight, height, goals) to create baseline fitness assessment.

Nutrition Agent: Generates meal plans tailored to user goals and preferences.

Exercise Agent: Creates workout routines based on available equipment and schedule.

Motivation Agent: Provides encouragement, goal-tracking support, and motivational tips.

Orchestrator Agent: Coordinates all agents and combines their outputs into a comprehensive fitness plan.

Agent Interactions:

Agents operate independently but share common user profile data.

Orchestrator manages workflow and ensures consistency across all outputs.

Each agent maintains its own internal data for session tracking or historical analysis.

Fallback mechanisms are included in case an AI service fails.

Workflow (Text-Based):

User Input → Assessment Agent → (Nutrition + Exercise + Motivation Agents) → Orchestrator → Complete Personal Plan

3. Tools, Libraries, and Frameworks Used

Frontend: Streamlit – for building a user-friendly web interface.

Programming Language: Python – used to implement all agents and orchestrator.

AI Integration: OpenAI GPT-3.5-turbo (free-tier) and optionally GPT-4 for ideal use.

Architecture: Custom multi-agent system using Python classes.

Agents operate independently.

Orchestrator manually coordinates outputs.

Communication is handled via direct method calls instead of external frameworks.

Data Storage: In-memory session data structures for temporary storage.

Note on Multi-Agent Frameworks:

Multi-agent frameworks like LangChain, CrewAI, or AutoGen provide built-in orchestration, messaging, and workflow management.

This project does not use these frameworks. All multi-agent logic is implemented in custom Python code to demonstrate agent collaboration.

4. LLM Selection

Ideal Choice: GPT-4 – best for nuanced, context-aware fitness and health recommendations.

Free-Tier Option: GPT-3.5-turbo – sufficient for generating fitness plans, nutrition advice, and motivational content.

Justification:
Health and fitness advice requires accurate, context-aware, and human-like responses. GPT-4 offers superior reasoning, while GPT-3.5 is suitable for prototype/demo purposes and cost-efficient.

5. Code and Deployment

GitHub Repository Structure:

fitness-coach-agents/
README.md
streamlit_app.py
orchestrator_agent.py
assessment_agent.py
nutrition_agent.py
exercise_agent.py
motivation_agent.py
requirements.txt


Deployment Options:

Streamlit Cloud (free tier)

Hugging Face Spaces

Railway or Render for simple deployment


6. Running Steps

Clone the repository:

git clone https://github.com/minnu1102/fitness agent.git


Navigate to the project folder:
cd fitness agents


Install dependencies:

pip install -r requirements.txt


Set OpenAI API Key:

export OPENAI_API_KEY="your_openai_api_key"
Run the Streamlit app:

streamlit run streamlit_app.py


Open the app in your browser:

Streamlit will provide a local URL (e.g., http://localhost:8501
) to access the app.

Enter user details:

Fill in name, age, weight, height, goals, activity level, days/week, and equipment.

Generate Fitness Plan:

Click the "Make My Plan" button to get a personalized plan including assessment, nutrition, exercise, and motivation.

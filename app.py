from orchestrator_agent import OrchestratorAgent
from assessment_agent import AssessmentAgent
from nutrition_agent import NutritionAgent
from exercise_agent import ExerciseAgent
from motivation_agent import MotivationAgent

# Create and start agents
assessor = AssessmentAgent()
assessor.start()

nutrition = NutritionAgent()
nutrition.start()

exercise = ExerciseAgent()
exercise.start()

motivation = MotivationAgent()
motivation.start()

# Orchestrator (brings all together)
orchestrator = OrchestratorAgent()
orchestrator.start(assessor, nutrition, exercise, motivation)
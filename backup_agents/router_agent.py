from uniassist_ai.gemini_client import classify_intent
from uniassist_ai.agents.meal_agent import MealAgent
from uniassist_ai.agents.gym_agent import GymAgent
from uniassist_ai.agents.shopping_agent import ShoppingAgent
from uniassist_ai.agents.travel_agent import TravelAgent
from uniassist_ai.agents.academic_agent import AcademicAgent

class RouterAgent:

    def __init__(self):
        self.meal = MealAgent()
        self.gym = GymAgent()
        self.shopping = ShoppingAgent()
        self.travel = TravelAgent()
        self.academic = AcademicAgent()

    def route(self, text: str):
        intent = classify_intent(text)
        print(f"[DEBUG] intent → {intent}")

        if intent == "meal":
            return self.meal.handle(text)
        elif intent == "gym":
            return self.gym.handle(text)
        elif intent == "shopping":
            return self.shopping.handle(text)
        elif intent == "travel":
            return self.travel.handle(text)
        elif intent == "academic":
            return self.academic.handle(text)
        else:
            return "❓ Could not classify your request."

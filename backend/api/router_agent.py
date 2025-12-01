from api.agents.meal_agent import MealAgent
from api.agents.gym_agent import GymAgent
from api.agents.travel_agent import TravelAgent
from api.agents.shopping_agent import ShoppingAgent
from api.agents.academic_agent import AcademicAgent

class RouterAgent:
    def __init__(self):
        self.agents = {
            "meal": MealAgent(),
            "gym": GymAgent(),
            "travel": TravelAgent(),
            "shopping": ShoppingAgent(),
            "academic": AcademicAgent(),
        }

    def route(self, message, agent_name):
        if agent_name not in self.agents:
            return "Invalid agent selected."

        agent = self.agents[agent_name]
        return agent.handle(message)

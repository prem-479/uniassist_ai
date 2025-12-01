from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from api.router_agent import RouterAgent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = RouterAgent()

class ChatRequest(BaseModel):
    message: str
    agent: str

@app.post("/chat")
def chat(req: ChatRequest):
    return router.route(req.message, req.agent)

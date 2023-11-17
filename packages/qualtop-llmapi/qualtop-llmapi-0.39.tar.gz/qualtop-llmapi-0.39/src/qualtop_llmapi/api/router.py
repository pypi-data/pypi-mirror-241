from qualtop_llmapi.api.routes import chat
from qualtop_llmapi.api.routes import embeddings
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(chat.router)
api_router.include_router(embeddings.router)

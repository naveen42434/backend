from fastapi import APIRouter
from app.api.speech_to_text import router as transcription_router

router = APIRouter()

@router.get("/healthcheck")
async def root():
    return {"status": "Ok"}

router.include_router(transcription_router, prefix="/transcribe", tags=["transcription"])
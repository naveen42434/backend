from fastapi import APIRouter
from app.api.speech_to_text import router as transcription_router
from app.api.text_to_speech import router as synthesize_router
from app.api.speech_service import router as speech_router

router = APIRouter()

@router.get("/healthcheck")
async def root():
    return {"status": "Ok"}

router.include_router(speech_router, prefix="/create_speech_service", tags=["speech_service"])
router.include_router(transcription_router, prefix="/transcribe", tags=["transcription"])
router.include_router(synthesize_router, prefix="/synthesize",tags=["synthesize"])
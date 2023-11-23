from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from app.utils.audio_utils import save_and_convert_audio, read_output_file, delete_files
from app.core.azure import transcribe_audio

router = APIRouter()

@router.post("/")
async def transcribe_audio_endpoint(file: UploadFile = File(...)):
    full_wav_path = save_and_convert_audio(file)
    transcribe_audio(full_wav_path)
    output_content = read_output_file()
    delete_files(['output.txt', full_wav_path])
    return JSONResponse(content={"message": "Transcription completed", "output": output_content}, status_code=200)
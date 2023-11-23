import os
from app.utils.file_reader import read_text_from_pdf, read_text_from_docx, read_text_from_txt
from app.core.synthesize import text_to_speech
from fastapi import APIRouter, File, UploadFile, HTTPException
from app.utils.delete import delete_files

router = APIRouter()

@router.post("/")
async def convert_text_to_speech(file: UploadFile = File(...), rate: int = 150):
    allowed_extensions = {'pdf', 'docx', 'txt'}
    file_extension = file.filename.split('.')[-1].lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Unsupported file type. Supported types: PDF, DOCX, TXT.")

    files_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'files')
    os.makedirs(files_folder, exist_ok=True)

    file_path = os.path.join(files_folder, file.filename)
    with open(file_path, "wb") as file_output:
        file_output.write(await file.read())

    if file_extension == 'pdf':
        text = read_text_from_pdf(file_path)
    elif file_extension == 'docx':
        text = read_text_from_docx(file_path)
    elif file_extension == 'txt':
        text = read_text_from_txt(file_path)

    output_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'synthesized_audio')
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, "synthesized_audio.wav")
    output_file_path = text_to_speech(text , output_path , rate=rate)

    delete_files("files", [file.filename])

    return {"message": "Text converted to speech successfully.", "audio_file": output_file_path}
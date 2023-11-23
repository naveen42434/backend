import os
from pydub import AudioSegment

AUDIO_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'audio')

def mp3_to_wav(mp3_file, wav_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")

def save_uploaded_file(file, file_name):
    file_path = os.path.join(AUDIO_FOLDER, file_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(file.read())

def save_and_convert_audio(file):
    file_name, file_extension = os.path.splitext(file.filename)
    file_name = file_name + '.wav'
    full_wav_path = os.path.join(AUDIO_FOLDER, file_name)

    if file_extension.lower() == '.mp3':
        mp3_to_wav(file.file, full_wav_path)
    else:
        save_uploaded_file(file.file, full_wav_path)

    return full_wav_path

def read_output_file():
    with open(os.path.join(AUDIO_FOLDER, 'Transcription.txt'), 'r') as output_file:
        return output_file.read()

def delete_files(files):
    for file_name in files:
        file_path = os.path.join(AUDIO_FOLDER, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
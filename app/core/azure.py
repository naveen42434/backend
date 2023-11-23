import threading
import os
import azure.cognitiveservices.speech as speechsdk
from app.core.config import settings

def transcribe_audio(file_path):
    subscription_key, region = settings.azure_subscription_key, settings.azure_region

    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    audio_config = speechsdk.AudioConfig(filename=file_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    def handle_recognized_speech(evt):
        with open(os.path.join(os.path.dirname(file_path), 'output.txt'), 'a') as file:
            file.write(evt.result.text)
        print("Recognized: {}".format(evt.result.text))

    def recognition_completed(evt):
        print("Transcription completed.")
        evt.set()

    transcription_complete_event = threading.Event()

    speech_recognizer.recognized.connect(handle_recognized_speech)
    speech_recognizer.session_stopped.connect(lambda evt: recognition_completed(transcription_complete_event))

    speech_recognizer.start_continuous_recognition()
    transcription_complete_event.wait()
    speech_recognizer.stop_continuous_recognition()
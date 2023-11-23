import pyttsx3

def text_to_speech(text,output_path, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.save_to_file(text, output_path)
    engine.runAndWait()

    return output_path
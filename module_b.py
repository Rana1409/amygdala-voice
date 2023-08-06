import whisper


def transcribe_audio(audio_file_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file_path)
    print(result["text"])
transcribe_audio(r"C:\Users\KIIT\Desktop\amyg_project\Real-Time-Voice-Cloning-master\samples\6829_00000.mp3")


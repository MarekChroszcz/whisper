import whisper

model = whisper.load_model("medium")
result = model.transcribe("C:\\Users\\Marek\\Documents\\Spotkanie.MP3", language="pl")

with open("C:\\Users\\Marek\\Desktop\\transkrypcja.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

import speech_recognition as sr

r = sr.Recognizer()

audio = sr.AudioFile("audio.wav")

with audio as source:
    audio = r.record(source)

text = r.recognize_google(audio)

with open("output.txt","w+") as f:
    f.write(text)


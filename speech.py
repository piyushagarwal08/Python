import speech_recognition as sr
audio_file = ("test.wav")
r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

try:
    print("audio file contains" + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError:
    print("Couldn't get the results from google")

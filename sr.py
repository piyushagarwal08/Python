import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Enter your search")
    audio=r.listen(source)
    print("search received")
    try:
        text = r.recognize_google(audio)
        print('You said : {}'.format(text))
    except Exception as e:
        print(e)

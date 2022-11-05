
import speech_recognition as sr
import pyttsx3
from datetime import datetime
from random import choice

myStrList = [
    'I want to Kneel',
    'Trust me I can do it',
    'Wait for sometime'
]

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        audio = r.listen(source, None, 3)

    try:
        print("Recognizing.........")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        if 'exit' in query or 'stop' in query:
            print(query)
            speak(query)
            speak(choice(myStrList))
        else:
            hour = datetime.now().hour
            if hour >= 21  and  hour < 6:
                speak("Good Night sir, take care")
            else:
                speak("Have a good day sir!")
            # exit()
    except Exception:
        speak("Sorry, I could not understand what you said, can you please repeat it again....")
        query = None
    return query

query = take_user_input()
print(f"query :{query}")
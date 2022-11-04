
import pyttsx3
from decouple import config
from datetime import datetime

Name, Company = "John Slater", "Marriot Grand"

engine = pyttsx3.init()

def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.now().hour
    print(f"hour :{hour}")

    if hour >= 6 and hour < 12:
        speak(f"Good Morning {Name}")
    elif hour >= 12 and hour <= 16:
        speak(f"Good Afternoon {Name}")
    elif hour >= 16 and hour < 19:
        speak(f"Good Evening {Name}")
    speak(f"I work for {Company}, How can I assist you?")

greet_user()

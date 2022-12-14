
import pyttsx3
from decouple import config
from datetime import datetime

Name, Company = config('Name'), config('Company')

engine = pyttsx3.init()

def speak(text):
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {Name}")
    elif (hour >= 12) and (hour  < 16):
        speak(f"Good Afternoon {Name}")
        print(f"Good Afternoon {Name}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {Name}")
    speak(f"I am calling from {Company}, How may help you?")
    print(f"I am calling from {Company}, How may help you?")

greet_user()

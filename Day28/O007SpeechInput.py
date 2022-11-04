
import speech_recognition as sr
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

def speak(text, gen):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[gen].id)
    engine.say(text)
    engine.runAndWait()

def take_user_input():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source, None, 3)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        if not 'exit' in query or not 'stop' in query:
            speak(query, 0)
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!", 0)
            else:
                speak("Have a good day sir!", 0)
            exit()
    except Exception:
        speak("Sorry, I could not understand, Could you please say again?", 0)
        query="None"
    return query

take_user_input()
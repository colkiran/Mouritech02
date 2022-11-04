import pyttsx3
import speech_recognition as sr

def onStart(name):
    print('starting :', name)

def onWord(name, location, length):
    print('word :', name, location, length)

def onEnd(name, completed):
    print("finishing :", name, completed)

engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

def speak(text):
    engine.say(text, "Richard")
    engine.runAndWait()

def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source, phrase_time_limit=3)

        try:
            print("Recognising.....")
            query = r.recognize_google(audio, language="en.in")
            print(query)
            speak(query)
        except Exception:
            print("Sorry, I could not understand, Could you please say again?")

take_user_input()
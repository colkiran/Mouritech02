
import pyttsx3

def InitEngine(eng):
    eng.setProperty('rate', 175)
    eng.setProperty('volume', 0.5)
    voices = eng.getProperty('voices')
    eng.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

engine = pyttsx3.init('sapi5')

InitEngine(engine)

speak("Hi this is Peter, Welcome to the grand launch event of our new car")
speak("Thanks for attending the event and making it a big success")
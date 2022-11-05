
import pyttsx3

def InitEngine(eng):
    eng.setProperty('rate', 175)
    eng.setProperty('volume', 0.5)
    voices = eng.getProperty('voices')
    eng.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

engine = pyttsx3.init('sapi5')

InitEngine(engine)

speak('I am proud to be an Indian')
speak("Mera bhaarathh mahaan")
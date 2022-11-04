
import pyttsx3

"""
pyttsx3 - supports both female and male voices which is provided by
sapi5- SAPI5 in windows
nsss - NSSpeechSynthesizer on MAC OS
espeak - eSpeak on every other platform
"""

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)

engine.setProperty('volume', 0.5)
text = 'the quick brown fox jumps over the lazy dog'

# set the voices of 0 - male and 1 - female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(text)
engine.runAndWait()

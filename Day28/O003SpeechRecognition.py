
import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 0.5)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Mera Bharath Mahaan")
engine.say("the quick brown fox jumps over the lazy dog")
engine.runAndWait()


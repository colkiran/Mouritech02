
import pyttsx3

engine = pyttsx3.init()

text = "I am proud to be an Indian"

engine.say(text)        # Queues a command to speak an utterance
engine.runAndWait()     # Block while processing all  currently queued commands



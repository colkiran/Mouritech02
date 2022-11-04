import pyttsx3

engine = pyttsx3.init()

text = "India is great"

engine.say(text)    # Queues the command to speak at utterance
engine.runAndWait() # Blocks while processing all currently queued commands


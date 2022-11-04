
import pyttsx3

class MySpeach:

    def __init__(self, driver='sapi5'):
        self.engine = pyttsx3.init(driver)
        eng = self.engine

    def word_per_minute(self, val):
        self.engine.setProperty('rate', val)

    def set_volume(self, val):
        self.engine.setProperty('volume', val)

    def male_voice(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def female_voice(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

ms = MySpeach()
ms.speak("the quick brown fox jumps over the lazy dog")

ms.female_voice()
ms.word_per_minute(100)
ms.set_volume(0.7)
ms.speak("the quick brown fox jumps over the lazy dog")

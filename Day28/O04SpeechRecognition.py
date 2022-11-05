
import pyttsx3

class MySpeech:
    def __init__(self, driver='sapi5'):
        self.engine = pyttsx3.init(driver)
        eng = self.engine


    def word_per_minute(self, speed):
        self.engine.setProperty('rate', speed)

    def set_volume(self, vol):
        self.engine.setProperty('volume', 'vol')

    def male_voice(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def female_voice(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)


    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

ms = MySpeech()

ms.speak("I am proud Indian")
ms.female_voice()
ms.word_per_minute(100)
ms.speak("India is great......")


import pyttsx3
import speech_recognition as sr

def onWord(name, location, length):
    print("word : ", name, location, length)

engine = pyttsx3.init()
engine.connect("started-word", onWord)

def speak(text):
    engine.say(text)
    engine.save_to_file(text, "myVoice.mp3")        # saves it to a file
    engine.runAndWait()

def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        audio = r.listen(source, phrase_time_limit=3)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(query)
        speak(query)
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')


take_user_input()
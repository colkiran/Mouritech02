import pyttsx3
import speech_recognition as sr
import os
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'performance': "C:\\Windows\\System32\\perfmon.exe",
    'word': "C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.exe",
    'excel': "C:\\Program Files\\Microsoft Office\\root\Office16\\EXCEL.exe"
}

engine = pyttsx3.init()


def open_notepad():
    os.startfile(paths['notepad'])


def open_calc():
    os.startfile(paths['calculator'])


def open_perfmon():
    os.startfile(paths['performance'])


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_word():
    os.startfile(paths['word'])

def open_excel():
    os.startfile(paths['excel'])
    # sp.run('start microsoft.windows.EXCEL:', shell=True)


def open__cmd_prompt():
    print("OPen Command")
    os.system('start cmd')


def open_prompt(cmd):
    if cmd == "notepad":
        open_notepad()
    elif cmd == "calculator":
        open_calc()
    elif cmd == "performance":
        open_perfmon()
    elif cmd == "camera":
        open_camera()
    elif cmd == "command":
        open__cmd_prompt()
    elif cmd == "word":
        open_word()
    elif cmd == "excel":
        open_excel()


def speak(text):
    engine.say(text)
    open_prompt(text)
    engine.runAndWait()


def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        audio = r.listen(source, phrase_time_limit=3)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(query)
        speak(query)
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')


take_user_input()

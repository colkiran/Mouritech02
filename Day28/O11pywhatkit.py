
import pywhatkit as pwk

def play_on_youtube(video):
    pwk.playonyt(video)

# play_on_youtube("kashmir mein tu kanyakumari")


def search_on_google(query):
    pwk.search(query)

# search_on_google("kholi fake fielding")

def send_whatsapp_message(number, message):
    pwk.sendwhatmsg_instantly(f"+91{number}", message)


send_whatsapp_message("9845251677", "Testing whatsapp messages....")
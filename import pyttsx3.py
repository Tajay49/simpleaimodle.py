import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)
    speak("Hello! This is James")

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is:")
    speak(time)

def date():
    now = datetime.datetime.now()
    speak("The current date is:")
    speak(now.strftime("%B %d, %Y"))

def greeting():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def wishme():
    speak("Welcome back!")
    time()
    date()
    greeting()
    speak("James at your service. Please tell me how I can help you.")

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    getvoices(0)  # Choose voice index: 0 for male, 1 for female
    wishme()
    while True:
        query = takeCommandMic().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break

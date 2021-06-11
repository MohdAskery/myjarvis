import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice

engine.setProperty('voice', voices[1].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Zira. Please tell me how may I help you")


def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    wishMe()
    speak("Hello. my NAME IS Mohd Askery")

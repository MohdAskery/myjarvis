import pyttsx3
import datetime
import getpass
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(f"hello {getpass.getuser()} how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Lestning....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"{query}\n")
    except Exception as ex:
        print("say again")
        return "None"
    return query


def send_email(to,con):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('techahideas@gmail.com','AskerY786.@')
    server.sendmail('techahideas@gmail.com', to, con)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            print("searching in 'wikipedia.........")
            query = query.replace("wikipedia", "")
            # results=wikipedia.summary(query,sentances=2)
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open w3school" in query:
            webbrowser.open("w3school.com")
        elif "quit" in query:
            print("thanks from using jarvis")
            speak("thanks from using jarvis")
            break
        elif "play music" in query:
            pat = r"F:\python code\voice\music"
            music = os.listdir(pat)
            print(music)
            os.startfile(
                os.path.join(pat, music[random.randint(0,
                                                       len(music) - 1)]))
        elif 'time' in query or 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "date" in query:
            today = date.today()
            speak(f"sir date is {today}")
        elif "vs code" in query:
            os.startfile(
                r"C:\Users\Kaiser\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            )
        elif "send email" in query:
            try:
                speak("What should I say?")
                con = takeCommand()
                to = "techahideas@gmail.com"
                send_email(to, con)
                speak(f"Email has send sucessfully to {to}")
            except Exception as e:
                print(e)
                speak("sorry email does't send ")

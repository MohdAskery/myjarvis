import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import getpass
from requests import get



#speak function
# ===============================================================
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

#Wish me Function
# ===============================================================
def wishMe():
    print("Hello This Is Jarvis")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

#Weather Function
# ===============================================================

def weather():
    from geopy.geocoders import Nominatim
    import requests, json
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "193121"
    API_KEY = "91e6f4c02561ca24cd070c4056df604d"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)

    geolocator = Nominatim(user_agent="geoapiExercises")
    zipcode = "193121"
    location = geolocator.geocode(zipcode)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        print(f"{CITY:-^30}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")
        speak(location)
        speak(f"Temperature: {temperature}")
        speak(f"Humidity: {humidity}")
        speak(f"Pressure: {pressure}")
        speak(f"Weather Report: {report[0]['description']}")
    else:
        print("Error in the HTTP request")
#Take Command
# ===============================================================

def takeCommand():
    print("Hello This Is Jarvis")
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query


# window.mainloop()
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif '.com' in query:
            webbrowser.open(query)

        elif '.net' in query:
            webbrowser.open(query)

        elif '.org' in query:
            webbrowser.open(query)

        elif '.in' in query:
            webbrowser.open(query)

        elif 'search on google' in query:
            query = query.replace("search on google", " ")
            webbrowser.open(query)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Mohd Askery Malik\\Desktop\\myjarvis\\music'
            songs = os.listdir(music_dir)
            # print(songs)
            print(os.path.splitext(songs[0])[0])
            speak(f" playing {os.path.splitext(songs[0])[0]}")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
           
        elif 'open cmd' in query:
            codePath = "C:\\Windows\\system32\\cmd.exe\\"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        
        elif 'weather' in query:
            weather()
        
        elif 'hello zara' in query:
            username = getpass.getuser()
            speak(f"Hello {username}")
       
        elif 'what is my ip' in query:
            ip = get('https://api.ipify.org').text
            print(f'My public IP address is: {ip}')
            speak(f'My public IP address is: {ip}')
        
        elif 'quit' in query:
            print("zara")
            exit()
        
        elif 'my name' in query:
            username = getpass.getuser()
            speak(f"your Name is {username}")
        else:
            print("Say that again please...")
            speak("Say that again please...")
            continue

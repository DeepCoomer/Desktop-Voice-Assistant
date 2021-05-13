import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import requests
import random
from sports import CRICKET as C

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour==0 and hour<12:
        speak("Good Morning!")

    elif hour==5 and hour<12:
        speak("Good Morning!")

    elif hour==12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak("Hii Sir I am Jarvis,how may I help You?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User said:",query,"\n")

    except Exception as e:
        # print(e)
        print("Please repeat again")
        return "none"
    return query

def Headlines():
    query_params = {
        "source": "The Times of India",
        "sortBy": "top",
        "apiKey": "d65ec3df76b0482bade20e7c2b295d08"
    }
    main_url = "https://newsapi.org/v2/top-headlines?country=in"

    res = requests.get(main_url,params=query_params)
    open_news = res.json()

    article = open_news["articles"]

    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        print(i+1,results[i])
    
    speak(results)


if __name__ == "__main__":
    wishme()
    while(True):
        query = takeCommand().lower()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        if 'ultimate' in query:
            speak("Udit is a great Shahyari writer but also a chutiya")
        elif 'open youtube' in query:
            url = 'youtube.com'
            webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
            webbrowser.get('firefox').open(url)
        elif 'open google classroom' in query:
            url = 'https://classroom.google.com/u/0/h'
            webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
            webbrowser.get('firefox').open(url)
        elif 'open google' in query:
            url = 'www.google.com'
            webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
            webbrowser.get('firefox').open(url)
        elif 'open whatsapp' in query:
            url = 'https://web.whatsapp.com/'
            webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
            webbrowser.get('firefox').open(url)
        elif 'news headlines' in query:
            Headlines()
        elif 'play movie' in query:
            rand = random.randint(0,8)
            movie_Dir = "C:\\Users\\DEEP COOMER\\Videos\\my movies"
            movies = os.listdir(movie_Dir)
            print(movies)
            os.startfile(os.path.join(movie_Dir,movies[rand]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is{strTime}")
        elif 'open notepad' in query:
            notepad_path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(notepad_path)
        elif 'open vs code' in query:
            vscode_path = "C:\\Users\\DEEP COOMER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscode_path)
        elif 'open word' in query:
            speak("Starting word")
            word_path = "C:\\Program Files\\WindowsApps\\Microsoft.Office.Desktop.Word_16051.13801.20360.0_x86__8wekyb3d8bbwe\\Office16\\WINWORD.EXE"
            os.startfile(word_path)
        elif 'shutdown' in query:
            speak("Shutting down laptop")
            os.system("shutdown /s /t 1")
        elif 'livescore' in query:
            print(C)

        if 'stop' in query:
            break




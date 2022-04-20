import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import smtplib

print("Initializing Jarvis...")
MASTER ="HARSH"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()
#wishme function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour<18:
        speak("Good AfterNoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)

    speak("I am Jarvis... How may I help you?")
#taking command from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio,language = "en-in")
        print(f"user said:{query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query
#main program begin from here
speak("Initializing Jarvis...")
wishMe()
while 1:
    def main():
        
        query = takeCommand()

        if "time" in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}") 
        elif "hello" in query.lower():
            speak(f"hello{MASTER}")
        elif "how are you" in query.lower():
            speak("I am fine... How are you?")
        elif "i am fine" in query.lower():
            speak(f"great{MASTER}")
        elif "who made you" in query.lower():
            speak("Harsh made me...")
        elif "where are you from" in query.lower():
            speak("I was made in Electro Coder laboratry in Ahmedabad Gujarat...")
        elif "thank you" in query.lower():
            speak(f"Welcome {MASTER}")
        elif "what is your born date" in query.lower():
            speak("My born date is 7th may 2020")
        elif "opencode" in query.lower():
            codePath = "C:\\Users\\U\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
    main()
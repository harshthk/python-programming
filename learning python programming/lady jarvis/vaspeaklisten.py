import os
import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import webbrowser
import wikipedia

print ("Initializing Jarvis...")
MASTER = "HARSH"

engine =pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source) 
        said = " "
        try:
            print("Recognizing")
            said = r.recognize_google(audio,language = "en-in")
            print(f"user said:{said}\n")
        except sr.UnknownValueError:
            print("Sorry,I did not get that")
            speak("Sorry,I did not get that")
            print("Please give command again")
            speak("Please give command again")
        except sr.RequestError:
            print("Sorry, my speech service is down")
            said = None
    return said

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

speak("Initializing Jarvis...")
if __name__ =="__main__":
    wishMe()
    
    while 1:
        def main():
            said = listen().lower()
            if "jarvis" in said.lower():
                speak("How can i help you...")
            elif "time" in said.lower():
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"{MASTER} the time is {strTime}") 
            elif "hello" in said.lower():
                speak(f"hello{MASTER}")
            elif "how are you" in said.lower():
                speak("I am fine... How are you?")
            elif "i am fine" in said.lower():
                speak(f"great{MASTER}")
            elif "who made you" in said.lower():
                speak("Harsh made me...")
            elif "where are you from" in said.lower():
                speak("I was made in Electro Coder laboratry in Ahmedabad Gujarat...")
            elif "thank you" in said.lower():
                speak(f"Welcome {MASTER}")
            elif "what is your born date" in said.lower():
                speak("My born date is 7th may 2020")
            elif "open code" in said.lower():
                codePath = "C:\\Users\\U\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif "search" in said.lower():#this command is not working
                search = " "
                search =speak("What do you want to search for")
                url = "https://google.com/search?q=" + search
                webbrowser.get().open(url)
                speak("Here is what I found for" + search)
            elif "wikipedia" in said.lower():
                speak("Searching in Wikipedia...")
                said = said.replace("wikipedia..."," ")
                result = wikipedia.summary(said, sentences=2)
                speak("According to wikipedia")
                print(result)
                speak(result)
            elif "open youtube" in said:
                speak(f"Opening Youtube for you {MASTER}...")
                webbrowser.open("https://youtube.com")
            
                
         main()


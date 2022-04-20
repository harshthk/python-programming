import speech_recognition as sr
from gtts import gTTS
import playsound
import time
import os

def speak(text):
    tts = gTTS(text=text,lang="en")
    filename = "v.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: "+ str(e))
    return said
text = get_audio()
if "hello" in get_audio:
    speak("Hello, How are you?")

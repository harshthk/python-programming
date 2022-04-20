import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random 
from gtts import gTTS
import webbrowser

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            sunny_speak(ask)
        audio = r.listen(source)
        voice_data=""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            sunny_speak("Sorry,I did not get that")
        except sr.RequestError:
            sunny_speak("Sorry, my speech service is down")
        return voice_data
def sunny_speak(audio_string):
    tts = gTTS(text=audio_string, lang ="en")
    r = random.randint(1,10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
def response(voice_data):
    if "what is your name" in voice_data:
        sunny_speak("My name is Sunny.")
    if "what time it is" in voice_data:
        sunny_speak(ctime())
    if "search" in voice_data:
        search =record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        sunny_speak("Here is what I found for" + search)

#time.sleep(1)
print("How can I help you?")
while 1:
    voice_data = record_audio()
    print(voice_data)
    response(voice_data)
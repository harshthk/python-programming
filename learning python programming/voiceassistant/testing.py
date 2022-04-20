import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")

MASTER = "Harsh..."

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait

speak("Initializing Jarvis...")

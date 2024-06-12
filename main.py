# This is main file
import pyttsx3
import speech_recognition

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Hello Sir")
speak("Hello Sir")


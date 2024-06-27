import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening.......")
        r.pause_threshold = 1
        r.energy_threshold = 500
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 0, 5)
    try:
        print("Processing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Not Get it, Say Again...")
        return "None"
    return query

# query = takeCmd()
# print(query)
# speak(query)
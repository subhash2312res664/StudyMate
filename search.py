# Here we defined function for Internet Search:
import wikipedia

from spktakecmd import speak
from spktakecmd import takeCmd

def whatis(query):
    speak("Searching wikipedia...")
    # query = query.replace("who is","")
    # query = query.replace("what is","")
    try:
        results = wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)
    except Exception as e:
        print("No speakable content available..")
        speak("No speakable content available")

def searchGoogle(query):
        import wikipedia
        import pywhatkit
        query = query.replace("hari","")
        query = query.replace("google search","")
        query = query.replace("google","")
        query = query.replace("search","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = wikipedia.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")





# query = input("Write query:")
# whatis(query)


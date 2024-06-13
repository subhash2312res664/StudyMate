# Here we defined function for Internet Search:
import wikipedia

from spktakecmd import speak
from spktakecmd import takeCmd

def whatis(query):
    print("Searching wikipedia...")
    speak("Searchin wikipedia...")
    query = query.replace("what is","")
    query = query.replace("Hey","")
    query = query.replace("Hari","")
    results = wikipedia.summary(query,sentences=2)
    speak(results)

# whatis()


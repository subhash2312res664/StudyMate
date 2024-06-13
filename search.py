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





# query = input("Write query:")
# whatis(query)


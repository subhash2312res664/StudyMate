# Here we defined function for Internet Search:
import wikipedia
import pywhatkit
import webbrowser
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

def searchYoutube(query):
        speak("This is what I found")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("hari","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        # pywhatkit.playonyt(query)
        speak("Done, Sir")


def plyYoutube(query):
    speak("This is what I found")
    query = query.replace("youtube search", "")
    query = query.replace("youtube", "")
    query = query.replace("hari", "")
    # web = "https://www.youtube.com/results?search_query=" + query
    # webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done, Sir")

def searchMoodle():
    # if "moodle" in query:
        speak("Opening IIT Patna Moodle..!")
        web  = "https://cet.iitp.ac.in/moodle/?redirect=0"
        webbrowser.open(web)
        speak("Done, Sir, Focus on your Study, Best of Luck!!")





# query = input("Write query:")
# whatis(query)


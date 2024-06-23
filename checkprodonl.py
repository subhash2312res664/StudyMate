import webbrowser
from spktakecmd import speak
def getpriceon(query):
    query = query.replace('hari','')
    query = query.replace('price of', '')
    query = "https://www.amazon.in/s?k=" + query
    webbrowser.open(query)
    speak("This is what, I found on Amazon")



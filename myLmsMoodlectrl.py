# Here we write code for our LMS Moodle,:
import webbrowser
from spktakecmd import speak

def searchMoodle():
    speak("Opening IIT Patna Moodle..!")
    web = "https://cet.iitp.ac.in/moodle/?redirect=0"
    webbrowser.open(web)
    speak("Done, Sir, Focus on your Study, Best of Luck!!")
def moodle(query):
    #

# Here we write code for our LMS Moodle,:
import webbrowser
import pyautogui as pt
from spktakecmd import speak

def searchMoodle():
    speak("Opening IIT Patna Moodle..!")
    web = "https://cet.iitp.ac.in/moodle/?redirect=0"
    webbrowser.open(web)
    speak("Done, Sir, Focus on your Study, Best of Luck!!")
def moodle(query):
    if "go to home" in query:
        img = pt.locateCenterOnScreen('img/home.png')
        pt.doubleClick(img)
        speak('Done')
    elif "go to dashboard" in query:
        img = pt.locateCenterOnScreen('img/dashboard.png')
        pt.doubleClick(img)
    elif "go to my courses" in query:
        img = pt.locateCenterOnScreen('img/my_courses.png')
        pt.doubleClick(img)
    elif "go to cet iit patna" in query:
        img = pt.locateCenterOnScreen('img/cet_iit_patna.png')
        pt.doubleClick(img)
    elif "go to central library" in query:
        img = pt.locateCenterOnScreen('img/central_library.png')
        pt.doubleClick(img)
    elif "go to academic portal" in query:
        img = pt.locateCenterOnScreen('img/academics_portal.png')
        pt.doubleClick(img)

    #

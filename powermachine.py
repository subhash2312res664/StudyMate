import os
from spktakecmd import speak
from time import sleep

def powrstm(query):

    if "shutdown the system" in query:
        speak("Are You sure you want to shutdown")
        speak("Conferm to Press Y or N")
        shutdown = input("Do you wish to shutdown your computer? (y/n)")
        if shutdown == "y":
            os.system("shutdown /s /t 1")
        elif shutdown == "no":
            print("Ok Sir")
            speak("Ok Sir")


    elif "restart the system" in query:

        speak("Are You sure you want to restart")
        speak("Conferm to press Y or N.")
        shutdown = input("Do you wish to shutdown your computer? (y/n)")
        if shutdown == "y":
            os.system("shutdown /r /t 1")
        elif shutdown == "n":
            print("Ok Sir")
            speak("Ok Sir")

    elif "lock the system" in query or "slip the system" in query or "sleep the system" in query or "slip di system" in query:
        import pyautogui as pt
        pt.hotkey('win', 'x')
        sleep(0.2)
        pt.press('u')
        sleep(0.2)
        pt.press('s')


    # elif "sleep the system" in query:



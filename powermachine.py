import os
from spktakecmd import speak

def powrstm(query):

    if "shutdown the system" in query:
        speak("Are You sure you want to shutdown")
        shutdown = input("Do you wish to shutdown your computer? (y/n)")
        if shutdown == "y":
            os.system("shutdown /s /t 1")
        elif shutdown == "no":
            print("Ok Sir")
            speak("Ok Sir")


    elif "restart the system" in query:
        speak("Are You sure you want to restart")
        shutdown = input("Do you wish to shutdown your computer? (y/n)")
        if shutdown == "y":
            os.system("shutdown /r /t 1")
        elif shutdown == "n":
            print("Ok Sir")
            speak("Ok Sir")

    elif "sleep the system" in query:



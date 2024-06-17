# This is main file
import webbrowser
import pywhatkit

import pyttsx3
import speech_recognition as sr

from spktakecmd import speak
from spktakecmd import takeCmd

if __name__ == "__main__":
    print("Hey, I am Hari, and welcome in Virtual world!!..")
    speak("Hey, I am HARI, and welcome in, Virtual world")
    Hari_ord = "I am Hari, How can i Assist you?."


    while True:
        query = takeCmd().lower()
        if "wake up" in query:
            from greetme import greet
            print(f"Hello, {greet()} Sir.")
            speak(f"Hello, {greet()} Sir.")
            print("How can i help you?")
            speak("How can i help you?")

            while True:
                query = takeCmd().lower()
                if "go to sleep" in query:
                    print("Ok Sir, I'm going to Sleep")
                    speak("Ok Sir, I'm going to Sleep")
                    break

                elif "hello" in query:
                    print("Yes Sir")
                    speak("Yes Sir")

                elif "stop this program" in query:
                    print("Ok Sir, I am going to stop this Program.")
                    speak("Ok Sir, I am going to stop this Program.")
                    exit()

                elif "who are you" in query or "hu r u" in query:
                    print("I am Hari")
                    speak("I am Hari")

                elif "how are you" in query or "how r u" in query:
                    print("I am fine")
                    speak("I am fine")

                elif "thanks" in query or "thank you" in query:
                    print("You're welcome Sir")
                    speak("you're Welcome Sir")

                elif "who created you" in query:
                    print(
                        "I am Created under a Capstone Project-I, by the CSDA [23-2026] Students of IIT Patna, group of 16th.")
                    speak("I am Created under a Capstone Project, by the CSDA Students of IIT Patna, group of 16th.")

                elif "members in group 16" in query:
                    members = ["Subhash Kumar Rana", "Aanchal Kumari", "Saurav Kumar", "Rajesh Kumar", "Suyansh Kumar"]
                    print(f"There are {len(members)} members in group 16:\n",
                          f"{members[0:]}")
                    speak(f"There are {len(members)} members in group 16:\n")
                    speak(f"{members[0:]}")

                elif "what is" in query or "who is" in query:
                    from search import whatis

                    whatis(query)

                elif "open google" in query:
                    webbrowser.open("www.google.com")
                elif "search google" in query:
                    from search import searchGoogle
                    searchGoogle(query)
                elif "open youtube" in query:
                    webbrowser.open('https://www.youtube.com/')

                elif "search youtube" in query:
                    from search import searchYoutube

                    searchYoutube(query)
                elif "play youtube" in query:
                    from search import plyYoutube

                    plyYoutube(query)

                elif "open" in query:
                    from openandcloseapp import openapp

                    openapp(query)

                elif "close" in query:
                    from openandcloseapp import closeapp

                    closeapp(query)

                elif "launch analysis file" in query:
                    import os
                    os.startfile("analysis.html")

                elif "launch salary predictor" in query:
                    import webbrowser
                    url = "https://salary-predictor-8qda.onrender.com/"
                    webbrowser.open(url)

                elif "time now" in query or "current time" in query:
                    import datetime

                    tmn = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Time is: {tmn}")
                    speak(f"Time is {tmn}")

                elif "moodle" in query or "model" in query:
                    from search import searchMoodle
                    searchMoodle()

                elif "shutdown the system" in query or "restart the system" in query or "sleep the system" in query:
                    from powermachine import powrstm

                    powrstm(query)

                elif "screenshot" in query or "capture screen" in query:
                    from screenshot import capturescreen
                    capturescreen()

                elif "ip address" in query:
                    from myipaddress import checkip
                    checkip()

                elif "source code" in query:
                    import webbrowser
                    url = "https://github.com/subhash2312res664/StudyMate"
                    webbrowser.open(url)
                    speak("This is the source code")

                elif "email" in query or "mail" in query:
                    from emailing import emailfn
                    emailfn()
                ######
                #Controller
                elif "minimize" in query or "maximize" in query:
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "type" in query or "enter" in query:
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "volumeup" in query or "volumedown" in query:
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "mute" in query or "unmute" in query:
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "play" in query or "pause" in query:
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "full screen window" in query or "exit full screen window" in query:
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "subtitles" in query or "captions" in query or "miniplayer" in query or "theater mode" in query:
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "scroll up" in query or "scroll down" in query or "fast scroll up" in query or "fast scroll down" in query:
                    from mouseandkeycontroller import controller
                    controller(query)


        elif "stop" in query:
            print("Done")
            speak("Done")
            exit()
















# query = takeCmd()
#
# print(query)
# speak(f"{query}")


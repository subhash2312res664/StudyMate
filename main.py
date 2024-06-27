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
    print("Say,Wake up to start or stop.")
    speak("Say, wake up to start or stop.")


    while True:
        query = takeCmd().lower()
        if "wake up" in query or "hari" in query or "start" in query:
            from greetme import greet
            print(f"Hello, {greet()} Sir.")
            speak(f"Hello, {greet()} Sir.")
            print("How can i help you?")
            speak("How can i help you?")

            while True:
                query = takeCmd().lower()
                if "go to sleep" in query:
                    print("Ok Sir, I'm going to Sleep, Say Wake Up to start.")
                    speak("Ok Sir, I'm going to Sleep, Say Wake Up to start.")
                    break

                elif "hello" in query:
                    print("Yes Sir")
                    speak("Yes Sir")

                elif "stop this program" in query or "close this program" in query:
                    print("Ok Sir, I am going to stop this Program.")
                    speak("Ok Sir, I am going to stop this Program.")
                    exit()

                elif "who are you" in query or "hu r u" in query:
                    print("I am Hari")
                    speak("I am Hari")

                elif "how are you" in query or "how r u" in query:
                    print("I am fine")
                    speak("I am fine")

                elif "thanks" in query or "thank you" in query or "thank" in query or "thank u" in query:
                    print("You're welcome Sir")
                    speak("you're Welcome Sir")

                elif "who created you" in query:
                    print(
                        "I am Created under a Capstone Project-I, by the CSDA [23-2026] Students of IIT Patna, group of 16th.")
                    speak("I am Created under a Capstone Project, by the CSDA Students of IIT Patna, group of 16th.")

                elif "members in group 16" in query:
                    members = ["Subhash Kumar Rana", "Aanchal Kumari", "Saurav Kumar", "Rajesh Kumar", "Suyash Kumar"]
                    print(f"There are {len(members)} members in group 16:\n",
                          f"{members[0:]}")
                    speak(f"There are {len(members)} members in group 16:\n")
                    speak(f"{members[0:]}")

                elif "what is" in query or "who is" in query or "wikipedia" in query:
                    from search import whatis
                    whatis(query)

                elif "price of" in query:
                    from checkprodonl import getpriceon
                    getpriceon(query)

                elif "translate" in query:
                    from deep_translate import translatelang
                    translatelang()

                elif "how to save a notepad message" in query or "how to save notepad message" in query:
                    from showhowto import howto
                    howto()

                elif "unit conversion" in query:
                    from unitconvertor import untcnv
                    untcnv()

                elif "open google" in query:
                    webbrowser.open("www.google.com")
                elif "search google" in query:
                    from search import searchGoogle
                    searchGoogle(query)

                elif "moodle" in query or "model" in query:
                    from myLmsMoodlectrl import searchMoodle
                    searchMoodle()

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

                elif "go back" in query or "escape" in query or "minimise all window" in query:
                    from mouseandkeycontroller import controller
                    controller(query)

                elif "launch analysis file" in query or "analysis" in query:
                    import webbrowser
                    import os
                    abs_path = os.path.abspath("analysis.html")
                    webbrowser.open(f'file://{abs_path}')
                    # os.startfile("analysis.html")

                elif "launch salary predictor" in query or "salary predictor" in query:
                    from salaryPredictor import salaryPre
                    salaryPre()

                elif "time now" in query or "current time" in query:
                    from CurrentTimeandDate import curr_time
                    curr_time()

                elif "today date" in query or "current date" in query:
                    from CurrentTimeandDate import curr_date
                    curr_date()

                elif ("shutdown the system" in query or "restart the system" in query or
                      "sleep the system" in query or "slip the system" in query or
                      "lock the system" in query or "slip di system" in query):
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

                elif "whatsapp" in query or "send message" in query:
                    from Whatsappmessage import cnfmsg
                    cnfmsg()

                elif "email" in query or "mail" in query:
                    from emailsmtp import sendemail
                    sendemail()

                elif "minimize" in query or "minimise" in query or "maximize" in query or "maximise":
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "restore" in query:
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "type" in query or "write" in query or "enter" in query:
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "volumeup" in query or "volume up" in query or "volumedown" in query or "volume down" in query:
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
                elif ("subtitles" in query or "captions" in query or "miniplayer" in query or "mini player" in query or
                      "theater mode" in query or "theatre mode" in query or "theatre mod" in query):
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "scroll up" in query or "scroll down" in query or "fast scroll up" in query or "fast scroll down" in query:
                    from mouseandkeycontroller import controller
                    controller(query)
                elif "crop screen" in query:
                    from mouseandkeycontroller import controller
                    controller(query)

                elif ("save" in query or "select all" in query or "all select" in query or "bold" in query or
                      "copy" in query or "duplicate" in query or 'bookmark' in query or "centre" in query or
                      "match next" in query or "find next" in query or "italic" in query or "download" in query or
                      "hyperlink" in query or "address bar" in query or "new window" in query or "new document" in query or
                      "refress the page" in query or "underline" in query or "paste" in query or "pest" in query or
                      "cut" in query or "redo" in query or "undo" in query):
                    from mouseandkeycontroller import controller
                    controller(query)



        elif "stop" in query or "cancel" in query:
            print("Done")
            speak("Done")
            exit()




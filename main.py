# This is main file
import webbrowser

import pyttsx3
import speech_recognition as sr

from spktakecmd import speak
from spktakecmd import takeCmd

if __name__ == "__main__":

    from greetme import greet
    print(f"Hello, {greet()} Sir.")
    speak(f"Hello, {greet()} Sir.")
    print("How can i help you?")
    speak("How can i help you?")

    while True:
        query = takeCmd().lower()
        if "hello" in query:
            print("Yes Sir")
            speak("Yes Sir")

        elif "stop this program" in query:
            print("Ok Sir, I am going to stop this Program.")
            speak("Ok Sir, I am going to stop this Program.")
            exit()

        elif "who are you" in query:
            print("I am Hari")
            speak("I am Hari")
        elif "hu r u" in query:
            print("I am Hari")
            speak("I am Hari")

        elif "how are you" in query:
            print("I am fine")
            speak("I am fine")
        elif "how r u" in query:
            print("I am fine")
            speak("I am fine")

        elif "who created you" in query:
            print("I am Created under a Capstone Project-I, by the CSDA [23-2026] Students of IIT Patna, group of 16th.")
            speak("I am Created under a Capstone Project, by the CSDA Students of IIT Patna, group of 16th.")

        elif "members in group 16" in query:
            members = ["Subhash Kumar Rana", "Aanchal Kumari", "Saurav Kumar", "Rajesh Kumar", "Suyansh Kumar"]
            print(f"There are {len(members)} members in group 16:\n",
                  f"{members[0:]}")
            speak(f"There are {len(members)} members in group 16:\n")
            speak(f"{members[0:]}")

        elif "what is" in query:
            from search import whatis
            whatis(query)

        elif "who is" in query:
            from search import whatis
            whatis(query)









# query = takeCmd()
#
# print(query)
# speak(f"{query}")


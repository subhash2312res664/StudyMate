import webbrowser
import pywhatkit
import pyautogui
import os

from spktakecmd import speak

dictapp = {"paint":"mspaint","commandprompt":"cmd","vscode":"code","word":"winword","chrome":"chrome","excel":"excel",
           "powerpoint":"powerpnt","brave":"brave","file manager":"explorer","notepad":"notepad"}

def openapp(query):
    speak("Lounching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("www","")
        query = query.replace("open","")
        query = query.replace("hari","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

                #or os.startfile(application_path)
                #path: "c:/Window/system32/notepad.exe"
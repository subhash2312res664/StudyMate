import webbrowser
import pywhatkit
import pyautogui
import time
import os

from spktakecmd import speak

dictapp = {"paint":"mspaint","commandprompt":"cmd","vscode":"code","word":"winword","calculator":"calc","chrome":"chrome","excel":"excel",
           "powerpoint":"powerpnt","brave":"brave","file manager":"explorer","notepad":"notepad"}

def openapp(query):
    if ".com" in query or ".co.in" in query or ".org" in query:
        speak("Lounching, sir")
        query = query.replace("www","")
        query = query.replace("open","")
        query = query.replace("hari","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    elif "setting" in query:
        speak("Lounching, sir")
        import pyautogui as pt
        pt.hotkey('win','i')
    elif "task manager" in query:
        speak("Lounching, sir")
        import pyautogui
        pyautogui.hotkey("ctrl","shift","esc")
    elif "model" in query:
        speak("Opening IIT Patna Moodle..!")
        web = "https://cet.iitp.ac.in/moodle/?redirect=0"
        webbrowser.open(web)
        speak("Done, Sir, Focus on your Study, Best of Luck!!")
    elif "library" in query:
        speak("Opening in My Loft Library..!")
        web = "https://app.myloft.xyz/user/login"
        webbrowser.open(web)
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                speak("Lounching, sir")
                os.system(f"start {dictapp[app]}")

                #or os.startfile(application_path)
                #path: "c:/Window/system32/notepad.exe"



def closeapp(query):
    query = query.replace("close","")

    if "one tab" in query or "1 tab" in query:
        # speak("Closing,sir")
        pyautogui.hotkey("ctrl", "w")
        speak("Done")
    elif "window" in query:
        # speak("Closing,sir")
        import pyautogui as pt
        pt.hotkey('alt','f4')
    elif "two tab" in query or "2 tab" in query or "to tab" in query:
        # speak("Closing,sir")
        for i in range(2):
            pyautogui.hotkey("ctrl", "w")
            time.sleep(0.5)
        speak("Done")
    elif "three tab" in query or "3 tab" in query:
        # speak("Closing,sir")
        for i in range(3):
            pyautogui.hotkey("ctrl", "w")
            time.sleep(0.5)
        speak("Done")

    elif "four tab" in query or "4 tab" in query:
        # speak("Closing,sir")
        for i in range(4):
            pyautogui.hotkey("ctrl", "w")
            time.sleep(0.5)
        speak("Done")
    elif "five tab" in query or "5 tab" in query:
        # speak("Closing,sir")
        for i in range(5):
            pyautogui.hotkey("ctrl", "w")
            time.sleep(0.5)
        speak("Done.")

    elif "all tab" in query:
        speak("Closing, Sir")
        import pyautogui as pt
        from time import sleep
        pt.hotkey('alt','space')
        sleep(0.2)
        pt.press('c')
        speak("Done Sir")

    elif "window" in query:
        speak("Closing, Sir")
        import pyautogui as pt
        from time import sleep
        pt.hotkey('alt', 'space')
        sleep(0.2)
        pt.press('c')
        speak("Done Sir")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                speak("Closing,sir")
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
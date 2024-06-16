import pyautogui as pt
from time import sleep

def controller(query):
    if "minimize" in query:
        pt.hotkey('alt','space')
        pt.press('n')
    elif "maximize" in  query:
        pt.hotkey('alt','space')
        pt.press('x')
    elif "type" in query:
        query = query.replace("type","")
        pt.typewrite(query,0.2)
    elif "volumeup" in query:
        for i in range(20):
            pt.press('volumeup')
    elif "volumedown" in query:
        for i in range(20):
            pt.press('volumedown')
    elif "mute" in query or "unmute" in query:
        pt.press('volumemute')


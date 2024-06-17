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
    elif "play" in query or "pause" in query:
        pt.press('k')
    elif "full screen window" in query or "exit full screen window" in query:
        pt.press('f11')
    elif "enter" in query:
        pt.press('enter')
    elif "subtitles" in query or "captions" in query:
        pt.press('c')
    elif "miniplayer" in query:
        pt.press('i')
    elif "theater mode" in query:
        pt.press('t')

    elif "scroll up" in query or "scroll down" in query:
        if "scroll up" in query:
            pt.moveTo(950, 510)
            for i in range(10):
                pt.scroll(50)
                sleep(0.1)
        if "scroll down" in query:
            pt.moveTo(950, 510)
            for i in range(10):
                pt.scroll(-50)
                sleep(0.1)
        if "fast scroll up" in query:
            pt.moveTo(950, 510)
            for i in range(10):
                pt.scroll(1000)
        if "fast scroll down" in query:
            pt.moveTo(950, 510)
            for i in range(10):
                pt.scroll(-1000)




    #





import pyautogui as pt
from time import sleep

def controller(query):
    if "minimize" in query or "minimise" in query:
        pt.hotkey('alt','space')
        pt.press('n')
    elif "maximize" in query or "maximise" in query:
        pt.hotkey('alt','space')
        pt.press('x')
    elif "restore" in query:
        pt.hotkey('alt','space')
        pt.press('r')
    elif "type" in query:
        query = query.replace("type","")
        pt.typewrite(query,0.2)
    elif "volumeup" in query or "volume up" in query:
        for i in range(10):
            pt.press('volumeup')
    elif "volumedown" in query or "volume down" in query:
        for i in range(10):
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
    elif "miniplayer" in query or "mini player" in query:
        pt.press('i')
    elif "theatre mode" in query or "theater mode" in query or "theatre mod" in query:
        pt.press('t')

    elif "go back" in query or "escap" in query:
        pt.hotkey('escape')

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

    elif "crop screen" in query:
        pt.hotkey('prtscr')
    elif "print" in query:
        pt.hotkey('ctrl','p')
    elif "save" in query:
        pt.hotkey('ctrl','s')
    elif "select all" in query or "all select" in query:
        pt.hotkey('ctrl','a')
    elif "bold" in query:
        pt.hotkey('ctrl','b')
    elif "copy" in query:
        pt.hotkey('ctrl','c')
    elif "duplicate" in query or 'bookmark' in query:
        pt.hotkey('ctrl','d')
    elif "centre" in query:
        pt.hotkey('ctrl','e')
    elif "find box" in query:
        pt.hotkey('ctrl','f')
    elif "match next" in query or "find next" in query:
        pt.hotkey('ctrl','g')
    elif "history" in query or "replace box" in query:
        pt.hotkey('ctrl','h')
    elif "italic" in query:
        pt.hotkey('ctrl', 'i')
    elif "download" in query:
        pt.hotkey('ctrl', 'j')
    elif "hyperlink" in query:
        pt.hotkey('ctrl', 'k')
    elif "address bar" in query:
        pt.hotkey('ctrl', 'l')
    elif "new window" in query or "new document" in query:
        pt.hotkey('ctrl', 'n')
    # elif "open file" in query:
    #     pt.hotkey('ctrl', 'o')
    elif "refress the page" in query:
        pt.hotkey('ctrl', 'r')
    elif "underline" in query:
        pt.hotkey('ctrl', 'u')
    elif "paste" in query or "pest" in query:
        pt.hotkey('ctrl', 'v')
    # elif "close current window" in query:
    #     pt.hotkey('ctrl', 'w')
    elif "cut" in query:
        pt.hotkey('ctrl', 'x')
    elif "redo" in query:
        pt.hotkey('ctrl', 'y')
    elif "undo" in query:
        pt.hotkey('ctrl', 'z')

    ##

    elif "minimise all window" in query:
        pt.hotkey('win','m')





    #





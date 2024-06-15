import os
import pyautogui
from datetime import datetime

from spktakecmd import speak

def capturescreen():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(desktop, filename)

    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    print(f"Screenshot saved to {filepath}")
    speak(f"Screenshot saved")

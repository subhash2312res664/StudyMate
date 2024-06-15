import requests

from spktakecmd import speak

def checkip():
    print("Searching...")
    speak("Searching")
    try:
        ip = requests.get("https://api.ipify.org").text
        print(ip)
        speak(f"Your Ip is: {ip}")
    except Exception as e:
        print("Weak Connection, Try agin.")
        speak("Weak Connection, Try agin.")

# checkip()

import pywhatkit as kit
import datetime
from spktakecmd import speak
from spktakecmd import takeCmd

def send_whatsapp_message(phone_number, message):
    # Get the current time
    now = datetime.datetime.now()
    # Schedule the message to be sent one minute later to allow time to open WhatsApp Web
    hour = now.hour
    minute = now.minute + 1

    try:
        # Use pywhatkit to send the message
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print(f"Message scheduled to {phone_number} at {hour}:{minute}")
    except Exception as e:
        print(f"An error occurred: {e}")


def cnfmsg():
    print("What is Recipient Whatsapp Number.:")
    speak("What is Recipient Whatsapp Number.:")

    while True:
        recipient_number = takeCmd()
        recipient_number = recipient_number.replace(" ", "")
        if "cancel" in recipient_number or "back" in recipient_number or "stop" in recipient_number:
            speak("Ok,Sir.")
            break
        if recipient_number.isdigit() and len(recipient_number) == 10:
            recipient_number = '+91' + recipient_number  # Assuming country code is '+91' for India
            break
        else:
            print("Please speak a valid 10 digit number, or say cance/back to go main menu")
            speak("Please speak a valid 10 digit number, or say cance to go main menu")


    print("What is the message?")
    speak("What is the message?")
    message_text = takeCmd()
    send_whatsapp_message(recipient_number, message_text)

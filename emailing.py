import smtplib
import time
from spktakecmd import speak
from spktakecmd import takeCmd

def sendEmail(user,password,to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(user,password)
    server.sendmail(user,to,content)

def emailfn():
    #
    try:
        # print("What is the sender Email?")
        # speak("What is the sender Email?")
        # time.sleep(0.5)
        # user = takeCmd().lower()
        # user = user.replace(" ","")
        # user = user + "@gmail.com"
        # # print(f"Sender Email:{user}")
        # # speak("This is the sender email.")
        # time.sleep(0.5)
        # print("Enter sender password:")
        # speak("Enter sender Password")
        # password = input()

        user = "indiansubhashkumar@gmail.com"
        password = "oobm qwul mgea ttvr"

        print("Please tell me the recipient's email address.")
        print("Example: sanjay235")
        speak("Please tell me the recipient's email address.")
        time.sleep(0.5)
        to = takeCmd().lower()
        to = to.replace(" ","")
        to = to + "@gmail.com"
        # print(f"Recipient Email:{to}")
        # speak("This is the Recipient Email.")
        speak("What is the message?")
        print("What is the message?")
        time.sleep(0.5)
        content = takeCmd()

        print("Here The Sender and Recipient email.")
        speak("Here The Sender and Recipient email")
        print(f"Sender Email:{user}")
        print(f"Recipient Email:{to}")
        print(f"Body Message:{content}")
        print("Are you sure to send, say yes or No for confermation")
        speak("Are you sure to send, say yes or no for confermation")
        conf = takeCmd()
        if conf == 'yes':
            sendEmail(user, password, to, content)
            print("Email has been sent Successfully!")
            speak("Email has been sent Successfully!")
        else:
            print("Ok, try next time")
            speak("Ok, try next time")

    except Exception as e:
        print(e)
        print("Sorry. I am not able to send this email")
        speak("Sorry. I am not able to send this email")


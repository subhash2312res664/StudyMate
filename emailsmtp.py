import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
import time
from spktakecmd import speak
from spktakecmd import takeCmd

def send_email(subject, body, reciver_email):
    sender_email = "indiansubhashkumar@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "indiansubhashkumar@gmail.com"
    password = "oobm qwul mgea ttvr"

    try:

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = reciver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)

        server.sendmail(sender_email, reciver_email, msg.as_string())
        server.quit()


        print("Email sent successfully!")
        speak("Email sent successfully!")
    except socket.gaierror as e:
        print(f"Failed to send email due to network error: {e}")
        speak(f"Failed to send email due to network error: {e}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        speak(f"Failed to send email: {e}")


def sendemail():
    #
    while True:
        speak("Please tell me the recipient's email address.")
        reciver_em = takeCmd()
        reciver_email_half = reciver_em.replace(" ", "")

        reciver_email = reciver_email_half + "@gmail.com"
        print(reciver_email)

        speak(f"You said {reciver_email} . Is that correct?  ")
        confirmation= takeCmd()
        print(f"Confirmation received: '{confirmation}'")
        if "yes" in confirmation or "correct" in confirmation:
            break

        else:
            speak("Okay, let's try again.")

    speak("What is the subject of the email?")
    subject = takeCmd()
    speak("What is the body of the email?")
    body = takeCmd()

    send_email(subject, body, reciver_email)
    speak("Email has been sent. How else can I assist you?")
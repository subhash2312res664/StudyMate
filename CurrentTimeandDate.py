from spktakecmd import speak
import datetime
def curr_time():
    now = datetime.datetime.now()

    current_time = now.strftime("%I:%M %p")  # 12-hour format with AM/PM

    print(f"Current time is {current_time}")
    speak(f"The current time is {current_time}")


def curr_date():
    now = datetime.datetime.now()

    current_date = now.strftime("%A, %d %B %Y")  # Full weekday name, day of month, full month name, year

    print(f"Today's date is {current_date}")
    speak(f"Today's date is {current_date}")
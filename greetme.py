
def greet():
    import datetime
    global grt
    hr = int(datetime.datetime.now().hour)

    if 0 <= hr < 12:
        grt = "Good Morning"
    elif 12 <= hr < 15:
        grt = "Good Afternoon"
    elif 15 <= hr < 20:
        grt = "Good Evening"
    else:
        grt = "Good Night"
    return grt
#
# greet()
# print(grt)
def timenow():
    import datetime
    from spktakecmd import speak
    tmn = datetime.datetime.now().strftime("%H:%M")
    print(f"Time is: {tmn}")
    speak(f"Time is {tmn}")

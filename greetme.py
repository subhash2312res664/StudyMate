import datetime

def greet():
    global grt
    hr = int(datetime.datetime.now().hour)

    if 0 <= hr < 12:
        grt = "Good Morning"
    elif 12 <= hr < 15:
        grt = "Good Afternoon"
    elif 15 <= hr < 20:
        grt = "Good Evening"
    elif 20 >= hr:
        grt = "Good Night"
    return grt

# greet()
# print(grt)
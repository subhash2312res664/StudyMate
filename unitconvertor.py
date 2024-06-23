from spktakecmd import speak
from spktakecmd import takeCmd

def unit_conversion(conversion_type,value):

    try:
        if "miles to kilometers" in conversion_type:
            result = value * 1.60934
        elif conversion_type == "kilometre to mile":
            result = value * 0.621371
        elif conversion_type == "kilometre to metre":
            result = value * 1000


        elif conversion_type == "metre to kilometre":
            result = value * 0.001
        elif conversion_type == "foot to meter":
            result = value * 0.3048

        elif conversion_type == "pound to kilogram" or "pounds to kg":
            result = value * 0.453592
        elif conversion_type == "kilogram to pound":
            result = value * 2.20462
        else:
            return None
        print(f"your answer is {result}")
        speak(f"your answer is {result}")
    except ValueError:
        print("Something went wrong.")



def untcnv():
    try:
        speak("tell me type of conversion")
        conversion_type = takeCmd().lower()
        print(conversion_type)
        speak("tell me value ")
        value_str = takeCmd().lower()

        value = int(value_str.split()[-1])
        print(value)
        unit_conversion(conversion_type, value)
    except Exception as e:
        print("Try Again..")

# untcnv()

import time
current_hour = int(time.strftime("%H"))


if current_hour>12:
    if current_hour<16:
        print("Good Afternoon")
    else :
        print("Good Evening")
else :
    print("Good Morning")
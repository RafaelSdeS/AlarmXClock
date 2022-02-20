from playsound import playsound
from datetime import datetime

#User's choice
h = input('Set the hour: ')
m = input('Set the minutes: ')

# Time in Hours and Mins
time = datetime.now()
hours = time.hour
minutes = time.minute
minutes = time.minute

#Hours can't be > 24 and min > 60
if int(h) >= 24 or int(m) >= 60:
    print('Wrong values for hour and/or minutes')
else:
    if int(h) >= int(hours):
        h1 = int(h) - int(hours)
    if int(m) >= int(minutes):
        m1 = int(m) - int(minutes)
    if int(h) < int(hours):
        h1 = 24 - (int(hours) - int(h))
    if int(m) < int(minutes):
        m1 = 60 - (int(minutes) - int(m))
        if int(h) >= int(hours):
            h1 = int(h) - int(hours)
        if int(h) < int(hours):
            h1 = 23 - (int(hours) - int(h))

    # The most important thing
    if int(h) == int(hours) and int(m) == int(minutes):
        playsound('alarm.mp3')
    else:
        while int(h) != int(hours) or int(m) != int(minutes):
            # Showing time for every While loop
            time = datetime.now()
            hours = time.hour
            minutes = time.minute
            print(time)
            # Time left untill the alarm
            print('There is left ', h1, ':', m1, 'untill the clock goes off')
            # The alarm
            if int(h) == int(hours) and int(m) == int(minutes):
              playsound("C:\\Users\\Rafael\\Documents\\Programação\\Python\\AlarmXClock\\alarmSound.mp3")








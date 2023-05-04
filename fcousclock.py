import time

def focus_timer(minutes):
    seconds = minutes * 60
    print("Focus timer started for", minutes, "minutes.")
    for i in range(seconds, 0, -1):
        time.sleep(1)
        mins, secs = divmod(i, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Time remaining:", timer, end="\r")
    print("Focus timer completed!")

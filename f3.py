import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"Focus time started for {minutes} minutes.")
    time.sleep(seconds)
    print("Focus time is over. Keep up the good work!")

focus_timer(25)

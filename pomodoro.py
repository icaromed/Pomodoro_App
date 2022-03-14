class Pomo(object):

    def __init__ (self, wakeup, sleep, lunch):

        self.wakeup = wakeup
        self.sleep = sleep
        self.lunch = lunch
    def __str__ (self):

        return f"Wake up at {self.wakeup}h\nLunch at {self.lunch}h\nSleep at {self.sleep}h"
    
wakeup  =input("When do you wanna wake up? (01-24)")
sleep = input("When do you wanna sleep (01-24)?")
lunch = input("When do you wanna lunch (01-24)?")

print(Pomo(wakeup,sleep,lunch))                                                                                                                                  
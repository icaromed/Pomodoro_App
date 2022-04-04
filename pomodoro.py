from datetime import datetime
from copy import copy
import time


class Pomodoro(object):
    def __init__(self):
        pass
    
    @staticmethod
    def pomodoro(number=4, duration=25, small_rest=5):
        # number=4, duration=25, small_rest=5

        def now():
            return datetime.now().strftime('%H %M %S').split()

        def pomo_run():
            stop = copy(now())
            stop[1] = int(duration) + int(stop[1])
            while stop[1] >= 60:
                stop[1] -= 60
                stop[0] = int(stop[0]) + 1
                while stop[0] >= 24:
                    stop[0] -= 24
            stop = list(map(lambda x: str(x), stop))
            stop = " ".join(stop)
            stop = datetime.strptime(stop, '%H %M %S').strftime('%H %M %S').split()
            print("\r\nPomo is running.")
            while now() != stop:
                time.sleep(1)
                print(":".join(now()))

            print("\r\nTake a rest!")
            input("Press Enter to start ")
            stop = copy(now())
            stop[1] = int(small_rest) + int(stop[1])
            while stop[1] >= 60:
                stop[1] -= 60
                stop[0] = int(stop[0]) + 1
                while stop[0] >= 24:
                    stop[0] -= 24
            stop = list(map(lambda x: str(x), stop))
            stop = " ".join(stop)
            stop = datetime.strptime(stop, '%H %M %S').strftime('%H %M %S').split()
            while now() != stop:
                time.sleep(1)
                print(":".join(now()))

        start = input("Do you want to start right now? (yes| no) ")
        if start == "yes".lower().strip():
            num = 0
            while num < number:
                input("\r\nPress Enter to start ")
                pomo_run()
                num += 1
            print("Take a long rest!")
        else:
            print("\r\nSee you later!")


if __name__ == "__main__":
    Pomodoro.pomodoro()

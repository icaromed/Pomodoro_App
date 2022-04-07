import time


class Pomodoro(object):
    def __init__(self):
        pass

    def pomodoro(self, number=4, duration=25, small_rest=5):
        self.start_pomo(number, duration, small_rest)

    def start_pomo(self, number, duration, small_rest):
        start = input("\r\nDo you want to start right now? (yes|no) ")
        if self.check_bool(start):
            num = 0
            while num < number:
                input("\r\nPress Enter to start your pomo")
                self.pomo_run(duration, small_rest)
                num += 1
            print("Take a long rest!")

    @staticmethod
    def pomo_run(duration, small_rest):
        stop = duration * 60
        print("\r\nPomo is running.")
        while stop > 0:
            if stop == 1:
                print(f"{stop} minute left")
            print(f"{stop} minutes left")
            time.sleep(60)
            stop -= 1

        input("\r\nPress Enter to start your rest")
        stop = small_rest * 60
        while stop > 0:
            if stop == 1:
                print(f"{stop} minute left")
            print(f"{stop} minutes left")
            time.sleep(60)
            stop -= 1

    @staticmethod
    def check_bool(question):
        return question.lower().strip() == "yes"


if __name__ == "__main__":
    Pomodoro().pomodoro()

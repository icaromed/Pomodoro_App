from sleep import Sleep
from datetime import datetime
from pomodoro import Pomodoro


class User(Sleep, Pomodoro):

    def __init__(self):
        self._name = input("What is your name? ")

        question = input("Would you like to create your custom routine schedule? (yes|no) ")
        if self.check_bool(question):
            super().__init__()
            print(self)
            self._avaiable_range = self.avaiable_range

    @staticmethod
    def initial_messages():
        print("\r\nLet's configurate your Pomo!")
        print("If you want, you can use our standard Pomo configurations (Just press Enter)")
        print("But if you prefer to configurate your Pomo (Pomo)")

    @property
    def name(self):
        return self._name

    def pomodoro_timer(self):
        right_now = int(datetime.now().strftime('%H'))
        if right_now in self._avaiable_range:
            print("Okay, it's time to Pomo!\r\n")

            question = input("Would you like to start your pomo? (yes|no) ")
            if self.check_bool(question):
                self.initial_messages()

                if input("What do you prefer? ").lower().strip() == "":
                    self.pomodoro()
                else:
                    number = int(input("How many pomodoros do you want to make before your long rest? "))
                    duration = int(input("How many minutes do you want your pomos to last? "))
                    small_rest = int(input("How many minutes do you want to rest between each pomo? "))
                    self.pomodoro(number, duration, small_rest)

        else:
            print("Well, it's not time for Pomo")
            print(self.next_pomo())

    def next_pomo(self):
        right_now = int(datetime.now().strftime('%H'))
        hours = int(self.wake_up) + int(self.sleep) - right_now
        return f"Your next pomo is in {hours} hours"


if __name__ == "__main__":
    conta = User()

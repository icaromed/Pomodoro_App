from sleep import Sleep
from datetime import datetime
from pomodoro import Pomodoro


class User(Sleep, Pomodoro):

    def __init__(self):

        self._name = input("What is your name? ")
        question = input("Would you like to create your custom routine schedule? (yes|no) ").lower().strip()
        if question == "yes":
            super().__init__()
            print(self)
            self._avaiable_range = self.activity_range()
        print(self.next_pomo())

    def pomodoro_timer(self):
        right_now = int(datetime.now().strftime('%H'))
        if right_now in self._avaiable_range:
            print("Okay, it's time to Pomo!\r\n")

            if input("Would you like to start your pomo? (yes|no) ").lower().strip() == "yes":
                print("\r\nLet's configurate your Pomo!")
                print("If you want you can use our standard Pomo configurations (Just press Enter)")
                print("But if you prefer to configurate your Pomo (Pomo)")

                if input("What do you prefer? ").lower().strip() == "":
                    self.pomodoro()
                # put the inputs here
                else:
                    number = 0
                    duration = 0
                    small_rest = 0
                    self.pomodoro(number, duration, small_rest)

        else:
            print("Well, it's not time for Pomo.")
            print(self.next_pomo())

    def next_pomo(self):
        right_now = int(datetime.now().strftime('%H'))
        hours = int(self.wake_up) + int(self.sleep) - right_now
        return f"Your next pomo is in {hours} hours."

    @property
    def name(self):
        return self._name


if __name__ == "__main__":
    conta = User()

#  fix pomodoro_timer
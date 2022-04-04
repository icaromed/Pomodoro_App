from sleep import Sleep
from datetime import datetime
from pomodoro import Pomodoro


class User(Sleep, Pomodoro):

    def __init__(self, hours_format=input("\r\nChoose you preference"
                                          ": ('12' for 12 hours format or '24' for 24 hours format) ")):

        super().__init__(hours_format)
        self._name = input("What is your name? ")
        self._avaiable_range = self.available_time()
        self.actual_time = int(datetime.now().strftime('%H'))

    def available_time(self):
        if input("Would you like to create your custom routine schedule? (yes|no) ").lower().strip() == "yes":

            super().__init__(input("\r\nChoose you preference"
                                   ": ('12' for 12 hours format or '24' for 24 hours format) "))
            if not self.error:
                self.sleeping()
                return self.activity_range()

    def pomodoro_timer(self):

        if self.actual_time in self._avaiable_range:
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
        time_h = self.actual_time
        hours = self._wake_up - time_h
        return f"Your next pomo is in {hours} hours."

    @property
    def name(self):
        return self._name


if __name__ == "__main__":
    conta = User()

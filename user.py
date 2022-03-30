from sleep import Sleep
from datetime import datetime
from pomodoro import Pomodoro


class User(Sleep, Pomodoro):
    
    def __init__(self):
        
        self._name = input("What is your name? ")
        self._avaiable_range = self.available_time()
        self.pomodoro_timer()

    def available_time(self):   
        if input("Would you like to create your custom routine schedule? (yes|no) ").lower().strip() == "yes":
            
            super().__init__(input("\r\nChoose you preference: ('12' for 12 hours format or '24' for 24 hours format) "))   
            if self.error == False:
                self.sleeping()
                return self.activity_range()
                
    def pomodoro_timer(self):
        self.actual_time = int(datetime.now().strftime('%H'))
        
        if self.actual_time in self._avaiable_range:
            print("Okay, it's time to Pomo!\r\n")
            
            if input("Would you like to start your pomo? (yes|no) ").lower().strip() == "yes":
                print("\r\nLet's configurate your Pomo!")
                print("If you want you can use our standard Pomo configurations (Just press Enter)")
                print("But if you prefer to configurate your Pomo (Pomo)")
                
                if input("What do you prefer? ").lower().strip() == "":
                    self.pomodoro()
                else:
                    number = 0
                    duration = 0
                    small_rest = 0
                    self.pomodoro(number, duration, small_rest)

        else:
            print("Well, it's not time for Pomo.")
            print(self.next_pomo)

    def next_pomo(self):
        time_h = self.actual_time
        hours = 0
        
        for _ in range(24):
            if time_h in self.available_range:
                return "Your next pomo is in {hours} hours."
            else:
                hours += 1
                time_h += 1



        
           
        
            

if __name__ == "__main__":
    
    conta = User()

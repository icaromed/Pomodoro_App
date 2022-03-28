from pomodoro import Pomo
from datetime import datetime

class User(Pomo):
    
    def __init__(self):
        
        self._name = input("What is your name? ")
        
        if input("Would you like to create your custom routine schedule? (yes|no) ").lower().strip() == "yes":
            
            super().__init__(input("\r\nChoose you preference: ('12' for 12 hours format or '24' for 24 hours format) "))   
            if self.error == False:
                self.sleeping()
                time_range = self.activity_range()
                actual_time = datetime.now().strftime('%H')
                
                if int(actual_time) in time_range:
                    print("Okay, time to Pomo!")
                else:
                    print("Well, it's not time for Pomo.")

           
        
            

if __name__ == "__main__":
    
    conta = User()

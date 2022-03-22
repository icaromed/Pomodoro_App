from pomodoro import Pomo
class User(Pomo):
    
    def __init__(self):
        self._name = input("What is your name? ")
        
        if input("Would you like to create your custom routine schedule? (yes|no) ").lower().strip() == "yes":
            super().__init__(input("\r\nChoose you preference: ('12' for 12 hours format or '24' for 24 hours format) "))
            

        

if __name__ == "__main__":
    User()
import pomodoro

def run():
       
    if input("Welcome to the Pomodoro Routine App\r\n\r\nWould you like to create your custom routine schedule? (yes|no) ").lower().strip() == "yes":
        user = pomodoro.Pomo(input("Choose you preference: ('12' for 12 hours format or '24' for 24 hours format) "))
        user.sleeping()
    
    print("\r\nThanks for using our app!")


if __name__ == "__main__":
    run()
#implementations:

#integrate customised pomodoro clock
#the creation of the schedule

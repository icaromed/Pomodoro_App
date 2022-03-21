import pomodoro

def run():
       
    if input("Welcome to the Pomodoro Routine App\r\n\r\nWould you like to create your custom routine schedule? (yes|no) ").lower().strip() == "yes":
        pomodoro.Pomo().sleeping()
    
    print("\r\nThanks for using our app.")


if __name__ == "__main__":
    run()

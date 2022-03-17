import pomodoro

def sleep():
    accept = input("Welcome to the Pomodoro Routine App\r\nWould you like to create your custom routine schedule? (yes|no) ").lower().strip()
    
    if accept == "yes":
        sleep_messages()
    
    print("Thanks for using our app.")

def sleep_messages():
    sleep_time = int(input("When do you wanna sleep? (01-24) "))
    sleep_hours = int(input("How many hours of sleep is good for you? (01-24) "))
    
    if sleep_hours > 24:
        if input("WoW! That's a lot of sleep.\r\nAre you sure about that? (yes|no) ").lower().strip()!="yes":
            sleep_messages()
    
    pomodoro.Pomo(sleep_time, sleep_hours).sleeping()


if __name__ == "__main__":
    sleep()

#implementations:

#choice of AM/PM or 24h
#fix error of str at input
#add sleep > 24 -- number of days
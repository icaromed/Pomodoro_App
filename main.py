from user import User 

def run():
       
    print("Welcome to the Pomodoro Routine App\r\n")

    #will call the creation of a new user
    user = User()
    
    print("\r\nThanks for using our app, {}!".format(user._name))


if __name__ == "__main__":
    
    run()


#implementations:

#integrate customised pomodoro clock
#the creation of the schedule
#what are the days of the week that you want to use this pomo?
#implement datetime

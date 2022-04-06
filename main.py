from user import User 


def run():
       
    print("Welcome to the Pomodoro Routine App\r\n")

    # will call the creation of a new user
    user = User()
    # user.pomodoro_timer()
    
    print("Thanks for using our app, {}!".format(user.name))


if __name__ == "__main__":
    
    run()


# implementations:

# integrate customised pomodoro clock
# the creation of the schedule
# what are the days of the week that you want to use this pomo?

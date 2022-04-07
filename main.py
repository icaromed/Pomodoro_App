from user import User 


def run():
       
    print("Welcome to the Pomodoro Routine App\r\n")

    # will call the creation of a new user
    new_user = User()
    new_user.pomodoro_timer()
    
    print("\r\nThanks for using our app, {}!".format(new_user.name))


if __name__ == "__main__":
    run()


# implementations:

# the creation of the schedule
# what are the days of the week that you want to use this pomo?

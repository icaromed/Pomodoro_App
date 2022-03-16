import pomodoro

def sleep():
    sleep_time = input("When do you wanna sleep? (01-24) ")
    sleep_hours = input("How much hours of sleep do you want? (01-24) ")

    print(pomodoro.Pomo(sleep_time, sleep_hours))
    print(pomodoro.Pomo(sleep_time, sleep_hours).remove_sleep_time())


if __name__ == "__main__":
    sleep()

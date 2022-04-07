from datetime import datetime


class Sleep(object):

    def __init__(self):

        q_sleep = input("When do you want to sleep? (01-24) ")
        q_wake_up = input("When do you want to wake up? (01-24) ")

        try:
            self._sleep = datetime.strptime(q_sleep, '%H').strftime('%H')
            self._wake_up = datetime.strptime(q_wake_up, '%H').strftime('%H')

        except ValueError:
            raise ValueError("Please insert a valid digit input")

    @property
    def avaiable_range(self):
        true_range = ([int(self.wake_up), int(self.sleep) - 1])
        return range(true_range[0], true_range[1])

    @property
    def sleep(self):
        return self._sleep

    @property
    def wake_up(self):
        return self._wake_up

    def __str__(self):
        return (f"\r\nGreat! So you're sleeping at {self.sleep}h "
                f"and waking up at {self.wake_up}h")


# for testing
if __name__ == "__main__":
    test = Sleep()

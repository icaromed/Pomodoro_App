class Pomo(object):
    def __init__ (self, sleep, sleep_hours):
        
        self.sleep = sleep
        while self.sleep > 24:
            self.sleep -= 24

        self.sleep_hours = sleep_hours
        while self.sleep_hours > 24:
            self.sleep_hours -= 24
        
        self.wake = self.sleep + self.sleep_hours
        while self.wake>24:
            self.wake -= 24

    def sleeping (self):
        print ("Great! So you're sleeping at {:}h and waking up at {:}h. Those are {:} hours of sleep."
        .format(self.sleep, self.wake,self.sleep_hours))
        if(input("Is that fine for you? (yes|no) ").lower().strip()!="yes"):
            sleep_hours = input("Type a new number of hours: ")



#for testing
if __name__=="__main__":
    pass  
    





                                                                                                                              
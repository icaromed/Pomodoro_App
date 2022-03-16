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

    def __str__ (self):
        return "Sleep at {:} h for {:} h.".format(self.sleep, self.sleep_hours)


    def remove_sleep_time(self):
        self.full_day = list(range(1,25))
        
        for position in range(1,self.sleep_hours):
            self.remove = self.sleep + position
            while self.remove > 24:
                self.remove -= 24 
            self.full_day.remove(self.remove)
        return "Sleep: {}h\r\nWakeup: {}h".format(self.sleep, self.wake)


#for testing
if __name__=="__main__":
    print(Pomo(1,6).remove_sleep_time())      
    





                                                                                                                              
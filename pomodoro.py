class Pomo(object):
    def __init__ (self, sleep, sleep_hours):

        self.sleep_hours = sleep_hours
        self.sleep = sleep

    def __str__ (self):
        return "Sleep at {}h for {} hours.".format(self.sleep, self.sleep_hours)


    def remove_sleep_time(self):
        self.full_day = list(range(1,25))
        for position in range(1,int(self.sleep_hours)):
            self.remove = int(self.sleep)+position
            if self.remove >24:
                self.remove -= 24 
            self.full_day.remove(self.remove)

        return "Sleep: {}h\r\nWakeup: {}h".format(self.full_day[-1],self.full_day[0])


#testing with 22 hours and 6 hours
if __name__=="__main__":
    print(Pomo(22,6).remove_sleep_time())      
    





                                                                                                                              
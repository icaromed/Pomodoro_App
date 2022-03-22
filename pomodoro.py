class Pomo():       
    
    def __init__ (self, hours_format):
        self.__hours_format = hours_format 
        
        self.__sleep = int(input("When do you wanna sleep? (01-24) "))

        self.__sleep_hours = int(input("How many hours of sleep is good for you? (01-24) "))

        self.__wake_up = self.__sleep + self.__sleep_hours

        self.sleeping()
    
    def sleeping (self):
        self.checking = False
        
        while self.checking == False:
            print ("Great! So you're sleeping at {:} and waking up at {:}. Those are {:} hours of sleep."
            .format(self.sleep, self.wake_up ,self.__sleep_hours))
            
            if(input("Is that fine for you? (yes|no) ").lower().strip()!="yes"):
                self.sleep_hours = int(input("Type a new number of sleeping hours: "))
            else:
                self.checking = True
                break
    
    @property
    def sleep(self):
        time = time_format(self, self.__sleep, self.__hours_format)
        return time
    
    @property
    def wake_up(self):
        self.__wake_up = self.__sleep + self.__sleep_hours
        time = time_format(self, self.__wake_up, self.__hours_format)
        return time
    
    @property
    def sleep_hours(self):
        time = time_format(self, self.__sleep_hours, self.__hours_format)
        return time

    @sleep_hours.setter
    def sleep_hours(self, new_hours):
        self.__sleep_hours = new_hours
    
    
    global time_format
    def time_format(self, time, format):
        while time > 24:
            time -=24
        if int(format) == 24:
            return "{}hrs".format(time)
        else:
            if 11 >= time >= 1:
                return "{} am".format(time)
            elif time >= 24:
                return "{} am".format(time)
            else:
                time -= 12
                return "{} pm".format(time)
    

#for testing
if __name__=="__main__":
    test = Pomo("12").sleeping()

#implementations:

#fix error of str at input   
                                                                                                                         
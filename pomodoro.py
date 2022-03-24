class Pomo():       
    
    def __init__ (self, hours_format):
        self.__hours_format = hours_format 
        
        self._sleep = int(input("When do you wanna sleep? (01-24) "))

        self.sleep_hours = int(input("How many hours of sleep is good for you? (01-24) "))

        self.__wake_up = self._sleep + self._sleep_hours

        self.sleeping()
    
    
    def sleeping (self):
        self.checking = False
        
        while self.checking == False:
            
            print (f"Great! So you're sleeping at {self.sleep[0]} {self.sleep[1]} " 
            f"and waking up at {self.wake_up[0]} {self.wake_up[1]}. Those are {self._sleep_hours} hours of sleep.")
            
            if(input("Is that fine for you? (yes|no) ").lower().strip()!="yes"):
                self.sleep_hours = int(input("Type a new number of sleeping hours: "))
            else:
                self.checking = True
                break
    
    @property
    def sleep(self):
        time = time_format(self, self._sleep, self.__hours_format)
        return time
    
    @property
    def wake_up(self):
        self.__wake_up = self._sleep + self._sleep_hours
        time = time_format(self, self.__wake_up, self.__hours_format)
        return time
    
    @property
    def sleep_hours(self):
        return self._sleep_hours

    @sleep_hours.setter
    def sleep_hours(self, new_hours):
        self._sleep_hours = new_hours  
    
    global time_format
    def time_format(self, time, format):
        while time > 24:
            time -=24
        if int(format) == 24:
            return (time, "hrs")
        else:
            if 11 >= time >= 1:
                return (time, "am")
            
            elif time >= 24 or time < 1:
                if time < 1:
                    pass
                else:
                    time -= 12
                return (time, "midnight")
            
            elif 13 > time:
                return (time, "noon") 
            
            else:
                time -= 12
                return (time, "pm")
    

#for testing
if __name__=="__main__":
    test = Pomo("12").sleeping()

#implementations:

#fix error of str at input   
                                                                                                                         
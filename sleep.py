from typing import ClassVar
from datetime import datetime

class Sleep():
    
    def __init__ (self, hours_format):
        self.__hours_format = hours_format
        self.error = False 
        
        try:
            self._sleep = int(input("When do you wanna sleep? (01-24) "))
            self.sleep_hours = int(input("How many hours of sleep is good for you? (01-24) "))
            self.__wake_up = self._sleep + self._sleep_hours
        except:
            print("\r\nType a valid number")
            self.error = True

        
    
    def sleeping (self):
        self.checking = False
        
        while self.checking == False:
            
            print (f"Great! So you're sleeping at {self.sleep[0]} {self.sleep[1]} " 
            f"and waking up at {self.wake_up[0]} {self.wake_up[1]}. Those are {self._sleep_hours} hours of sleep.")
            
            if(input("Is that fine for you? (yes|no) ").lower().strip()!="yes"):
                try:
                    self.sleep_hours = int(input("Type a new number of sleeping hours: "))
                except:
                    print("\r\nType a valid number")
                    self.error = True
            else:
                self.checking = True
    
    def activity_range(self):
        print_range = ([self.wake_up, self.sleep])
        true_range = ([self.__wake_up, self._sleep - 1])
        
        print(f"Your activity range is from {print_range[0][0]} {print_range[0][1]} to {print_range[1][0]} {print_range[1][1]}.\r\n")
        
        return range(true_range[0], true_range[1]) 
   
    @property
    def sleep(self):
        
        time = time_format(self, self._sleep, self.__hours_format)
        return time
    
    @property
    def wake_up(self):
        
        self.__wake_up = self._sleep + self._sleep_hours
        while self.__wake_up > 24:
            self.__wake_up -= 24  
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
            return (datetime.strptime(str(time), '%H').strftime('%H'), "hrs")
        
        else:
            if 11 >= time >= 1:
                return (datetime.strptime(str(time),'%H').strftime('%H'), "am")
            
            elif time >= 24 or time < 1:
                if time < 1:
                    pass

                else:
                    time -= 12
                return (datetime.strptime(str(time),'%H').strftime('%H'), "midnight")
            
            elif 13 > time:
                return (datetime.strptime(str(time),'%H').strftime('%H'), "noon") 
            
            else:
                time -= 12
                return (datetime.strptime(str(time),'%H').strftime('%H'), "pm")
    

#for testing
if __name__=="__main__":
    
    test = Sleep("12").sleeping()


#implementations:

#fix error of str at input   
                                                                                                                         
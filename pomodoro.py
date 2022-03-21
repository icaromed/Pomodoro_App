class Pomo(object):
    
    def __init__ (self):
        self.__name = input("What is your name? ")

        self.__sleep = (int(input("When do you wanna sleep? (01-24) ")))

        self.__sleep_hours = int(input("How many hours of sleep is good for you? (01-24) "))
    
    global time_ad
    @staticmethod 
    def time_ad(time):
        while time > 24:
            time -=24
        return time

    def sleeping (self):
        self.checking = False
        while self.checking == False:
            print ("Great! So you're sleeping at {:}h and waking up at {:}h. Those are {:} hours of sleep."
            .format(time_ad(self.__sleep), time_ad(self.__sleep + self.__sleep_hours) ,time_ad(self.__sleep_hours)))
            
            if(input("Is that fine for you? (yes|no) ").lower().strip()!="yes"):
                self.sleep_hours = int(input("Type a new number of sleeping hours: "))
            else:
                self.checking = True
    

    @property
    def sleep_hours(self):
        return self._Pomo__sleep_hours

    @sleep_hours.setter
    def sleep_hours(self, new_hours):
        self.__sleep_hours = new_hours

#for testing
if __name__=="__main__":
    test = Pomo().sleeping()

#implementations:

#choice of AM/PM or 24h
#fix error of str at input                                                                                                                            
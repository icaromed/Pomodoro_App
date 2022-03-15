class Pomo(object):

    def __init__ (self, wakeup, sleep, lunch):

        self.day = list(range(1,25))
        self.wakeup = wakeup
        self.sleep = sleep
        self.lunch = lunch
    
    def __str__ (self):
        return "Wake up at {}h\nLunch at {}h\nSleep at {}h".format(self.wakeup,self.lunch, self.sleep)
    
    
    def find_sleep(self):
        for position in range(1,int(self.wakeup)):
            self.remove = int(self.sleep)+position
            if self.remove >24:
                self.remove -= 24 
            self.day.remove(self.remove)
        return "Your sleep starts at {}h and finishs at {}h!".format(self.day[-1],self.day[0])

            
        




sleep = input("When do you wanna sleep (01-24)?")
wakeup = input("How much hours of sleep do you want? (01-24)")

x = Pomo(wakeup,sleep,lunch)
print(x.find_sleep())                                                                                                                                 


class Time:
    hour:int
    minute:int

    def __init__(self,hour,minute):
        self.hour = hour
        self.minute = minute
    
    def isValid(self):
        return self.hour < 24 and self.minute < 60

    def __add__(self,time):
        newTime = Time(self.hour,self.minute)
        newTime.minute += time.minute
        newTime.hour += time.hour
        
        if newTime.minute >= 60:
           newTime.minute -= 60
           newTime.hour += 1
        
        if newTime.hour >= 24:
            newTime.hour -= 24
        
        return newTime
         
    def __lt__(self,other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour and self.minute > other.minute:
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __repr__(self):
        return self.__str__()
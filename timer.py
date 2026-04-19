import time

# Controls the time system used to determine if pill time
class Timer:
    def __init__(self):
        self.last_time = 0
        self.current_time = 0
        self.delta = 0 # Counts seconds of each "day"
    
    # Called every tick in While True:
    # Sets delta
    def timeIncrement(self):
        self.current_time = time.ticks_ms()
        self.delta = time.ticks_diff(self.current_time, self.last_time)
        print(self.delta)
        if self.delta >= 20000:
            self.last_time = self.current_time
    
    def getIncrement(self):
        return self.delta
    
    def isPillTime(self):
        return self.delta >= 10000 and self.delta <= 20000
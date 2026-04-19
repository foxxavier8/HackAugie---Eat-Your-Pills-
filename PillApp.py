from machine import Pin
import time
from timer import Timer
from lcd_display import LCD

# Pin assignments
ledPin = Pin(15, Pin.OUT)
motionSensor = Pin(22, Pin.IN)
timer = Timer()
lcd = LCD()
disableRefill = False
lcd.printAllFull()
ledFlag = True # Tracks whether the Led can flash at start of pill time
eatenFlag = False


while True:
    reading = not motionSensor.value() # If 1, pills sensed
    
    if timer.isPillTime():
        if ledFlag:
            ledPin.value(1)
            time.sleep(0.1)
            ledPin.value(0)
            ledFlag = False
            
        if reading and not eatenFlag:
            disableRefill = True
            lcd.printEatPills()
        elif not disableRefill:
            lcd.printRefillPills()
        else:
            eatenFlag = True
            lcd.printAllFull()
    else:
        lcd.printAllFull()
        eatenFlag = False
        disableRefill = False
        ledFlag = True
        
    timer.timeIncrement()
    
    time.sleep(0.1)  # small delay to stabilize loop
    

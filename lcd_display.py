from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd  # requires LCD library

# I2C setup (adjust pins if needed)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

#LCD Display controller
class LCD:
    def __init__(self):
        # LCD setup
        I2C_ADDR = 0x27
        self.lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
        self.printed = -1 # Tracks last printed message, prevents repeated updates
        self.reset()
    
    # Clears lcd display
    def reset(self):
        self.lcd.move_to(0,0)
        self.lcd.putstr("               ")
        self.lcd.move_to(0,1)
        self.lcd.putstr("               ")
        
    def printEatPills(self):
        if not self.printed == 1:
            self.reset()
            self.lcd.move_to(3,0)
            self.lcd.putstr("Eat Pills")
            self.printed = 1
    
    def printAllFull(self):
        if not self.printed == 0:
            self.reset()
            self.lcd.move_to(3,0)
            self.lcd.putstr("Don't Eat")
            self.printed = 0
    
    def printRefillPills(self):
        if not self.printed == 2:
            self.reset()
            self.lcd.move_to(2,0)
            self.lcd.putstr("Refill Pills")
            self.printed = 2
        
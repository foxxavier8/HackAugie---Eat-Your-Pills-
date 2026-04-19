from machine import Pin, I2C, ADC
import time
from pico_i2c_lcd import I2cLcd  # requires LCD library

# ADC setup (GPIO 26 = ADC0)
adc = ADC(26)

# I2C setup (adjust pins if needed)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# LCD setup
I2C_ADDR = 0x27
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# Pin assignments
buzzerPin = Pin(15, Pin.OUT)
ledPin = Pin(16, Pin.OUT)
motionSensor = Pin(22, Pin.IN)
last_time = 0
current_time = 0

while True:
    reading = motionSensor.value()
    current_time = time.ticks_ms()
    delta = time.ticks_diff(current_time, last_time)
    
    if delta > 10000:
        buzzerPin.value(0)
        lcd.move_to(3, 0)
        lcd.putstr("Eat Pills")

        for i in range(2):
            ledPin.value(1)
            time.sleep(0.1)
            ledPin.value(0)
            time.sleep(0.1)
            buzzerPin.value(0)
    
    if reading == 0:
        last_time = current_time
        lcd.move_to(3, 0)
        lcd.putstr("All full ")
    
    else:
        lcd.move_to(3, 0)
        lcd.putstr("All full ")
        buzzerPin.value(0)
        ledPin.value(0)
    
    time.sleep(0.1)  # small delay to stabilize loop
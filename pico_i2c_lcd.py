from lcd_api import LcdApi
from machine import I2C
import time

class I2cLcd(LcdApi):
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.backlight = 0x08

        self.init_lcd()

        super().__init__(num_lines, num_columns)

    def init_lcd(self):
        time.sleep_ms(20)
        self.write_cmd(0x03)
        time.sleep_ms(5)
        self.write_cmd(0x03)
        time.sleep_ms(5)
        self.write_cmd(0x03)
        time.sleep_ms(1)
        self.write_cmd(0x02)

        self.write_cmd(0x28)  # 4-bit mode, 2 lines
        self.write_cmd(0x0C)  # display on
        self.write_cmd(0x06)  # entry mode
        self.clear()

    def write_cmd(self, cmd):
        self.write_byte((cmd & 0xF0))
        self.write_byte((cmd << 4) & 0xF0)

    def write_data(self, data):
        self.write_byte((data & 0xF0) | 0x01)
        self.write_byte((data << 4) & 0xF0 | 0x01)

    def write_byte(self, data):
        self.i2c.writeto(self.i2c_addr, bytes([data | self.backlight]))
        self.i2c.writeto(self.i2c_addr, bytes([data | self.backlight | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytes([data | self.backlight]))

    def clear(self):
        self.write_cmd(0x01)
        time.sleep_ms(2)

    def move_to(self, col, row):
        addr = col + (0x40 * row)
        self.write_cmd(0x80 | addr)

    def putchar(self, char):
        self.write_data(ord(char))
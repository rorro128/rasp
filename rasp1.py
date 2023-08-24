from time import sleep
import board
import nmap
from digitalio import DigitalInOut
from adafruit_character_lcd.character_lcd import Character_LCD_Mono

lcd_columns = 16
lcd_rows = 2
lcd_rs = DigitalInOut(board.D26)
lcd_en = DigitalInOut(board.D19)
lcd_d4 = DigitalInOut(board.D13)
lcd_d5 = DigitalInOut(board.D6)
lcd_d6 = DigitalInOut(board.D5)
lcd_d7 = DigitalInOut(board.D11)

lcd = Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

nm = nmap.PortScanner()
nm.scan('192.168.1.0/24', arguments="-T4 -F")
lcd.message = "holaaaa nmap"
sleep(4)

lcd.clear()
for x in nm.all_hosts():
    lcd.message = f"IP: {x}\n" + nm[f"{x}"]['addresses']['ipv4']
    #lcd.message = nm['{x}']['addresses']['mac']
    sleep(4)
    lcd.clear()


#for x in range(0, 16):
#    lcd.move_right()
#    sleep(.2)
#sleep(2)

#for x in range(0, 16):
#    lcd.move_left()
#    sleep(.2)
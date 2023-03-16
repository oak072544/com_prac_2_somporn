import smbus
import time
 
LED1 = 0x01
LED2 = 0x02
LED3 = 0x04
LED4 = 0x08
LED5 = 0x10
LED6 = 0x20
LED7 = 0x40
LED8 = 0x80
bus = smbus.SMBus(1)
 
while True:
	bus.write_byte(0x20, LED8)
	time.sleep(0.5)
	bus.write_byte(0x20, LED7)
	time.sleep(0.5)
	bus.write_byte(0x20, LED6)
	time.sleep(0.5)
	bus.write_byte(0x20, LED5)
	time.sleep(0.5)
	bus.write_byte(0x20, LED4)
	time.sleep(0.5)
	bus.write_byte(0x20, LED3)
	time.sleep(0.5)
	bus.write_byte(0x20, LED2)
	time.sleep(0.5)
	bus.write_byte(0x20, LED1)
	time.sleep(0.5)
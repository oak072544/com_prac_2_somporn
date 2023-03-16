from gpiozero import LED
from time import sleep
from gpiozero import Button

button = Button(2)
led1 = LED(25)
led2 = LED(8)
led3 = LED(7)
button.wait_for_press()

while True:
    led1.on()
    sleep(5)
    led2.on()
    sleep(2)
    led1.off()
    led2.off()
    led3.on()
    sleep(5)
    led3.off()
    led2.on()
    sleep(5)
    led2.off()
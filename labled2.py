from gpiozero import LED
from time import sleep
from gpiozero import Button

button = Button(2)
led = LED(25)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()
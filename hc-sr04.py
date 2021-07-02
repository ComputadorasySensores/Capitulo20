from machine import Pin
import utime

trigger = Pin(15,Pin.OUT)
echo = Pin(14, Pin.IN)
distancia = 0

while True:
    trigger.high()
    utime.sleep(0.00001)
    trigger.low()
    
    while echo.value() == 0:
        comienzo = utime.ticks_us()
    while echo.value() ==1:
        final = utime.ticks_us()
    
    duracion = final - comienzo
    distancia = (duracion * 0.0343) / 2
    print("Distancia:",distancia,"cm")
    utime.sleep(3)

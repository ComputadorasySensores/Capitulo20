from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

trigger = Pin(15,Pin.OUT)
echo = Pin(14, Pin.IN)
distancia = 0

# inicializa la pantalla
i2c = I2C(0,sda=Pin(0), scl=Pin(1),freq=40000)
oled = SSD1306_I2C(128,64,i2c)

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
    oled.fill(0)
    oled.text("Distancia:",0,2)
    oled.text(str(distancia) + " cm",0,17)
    oled.show()
    
    utime.sleep(3)

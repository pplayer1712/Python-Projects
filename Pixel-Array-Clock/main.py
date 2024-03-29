from machine import Pin, SPI
from machine import Timer
import max7219
from time import sleep
import machine
import utime
import time
import acTime

utime.sleep(2)
#init pixel-matrix
spi = SPI(0,sck=Pin(18),mosi=Pin(19))
cs = Pin(17, Pin.OUT)

display = max7219.Matrix8x8(spi, cs, 4)
display.brightness(1)

length = 32

utime.sleep(2)

curTime = acTime.getTime().split(':')
#asign variables
sec = int(curTime[2])
mnt = int(curTime[1])
hr = int(curTime[0])


def updateScreen():
    display.show()
    display.fill(0)

def clean(number):
    if number > 0  and number <= 9:
        return "0" + str(number)
    if number == 0:
        return "00"
    else:
        return str(number)
    
def tempereture():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
 
    while True:
        reading = sensor_temp.read_u16() * conversion_factor 
        temp = 27 - (reading - 0.706)/0.001721
        return str(round(temp, 0))
        utime.sleep(2)

#indicate a : every passing second
def cursor(option):
    if option == 1:
        display.text(clean(hr),-1,0,1)
        display.text(clean(mnt),17,0,1)
        display.text('',12,0,1)
        updateScreen()
    else:
        display.text(clean(hr),-1,0,1)
        display.text(clean(mnt),17,0,1)
        display.text(':',12,0,1)
        updateScreen()

#start timer to display acurate time
def time(timer):
    global hr
    global sec
    global mnt
    
    if hr >= 23 and mnt >= 59 and sec >= 59:
        hr = 0
        mnt = 0
        sec = -1
    if mnt >= 59 and sec >= 59:
        hr += 1
        mnt = 0
        sec = -1
    if sec >= 59:
        mnt += 1
        sec = -1
    sec = sec + 1
    print(str(hr) + " " + str(mnt) + " " + str(sec))
    
timer=Timer(-1)
timer.init(period=1000, mode=Timer.PERIODIC, callback=time)   #initializing the timer

#animate pixel matrix
while True:
    count = -31
    for i in range(20):
        cursor(1)
        sleep(0.5)
        cursor(0)
        sleep(0.5)
    
    for x in range(length):     
        display.fill(0)
        display.text(clean(hr), x - 1,0,1)
        display.text(clean(mnt), x + 17,0,1)
        display.show()
        sleep(0.1)
        
    for x in range(length):
        display.fill(0)
        display.text(tempereture(), count - 1,0,1)
        display.show()
        count += 1
        sleep(0.1)
        
    count = 0
    
    for i in range(5):
        display.text(tempereture(),-1,0,1)
        sleep(1)
        updateScreen()
        
    count = 1
    
    for x in range(length):
        display.fill(0)
        display.text(tempereture(), count - 1,0,1)
        display.show()
        count += 1
        print(count)
        updateScreen()
        sleep(0.1)
      
    count = -31
    
    for x in range(length):
        display.fill(0)
        display.text(clean(hr), count - 1,0,1)
        display.text(clean(mnt), count + 17,0,1)
        display.show()
        count += 1
        sleep(0.1)
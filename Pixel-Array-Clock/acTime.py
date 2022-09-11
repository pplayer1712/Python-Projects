import urequests
import machine
import network
import time


"""
led = machine.Pin("LED", machine.Pin.OUT)
led.on()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

for i in range(10):  
    if wlan.isconnected() != True:
        led.on()
        wlan.connect("Kein-Nordstream-P(2,4)", "DimP1712#")
        time.sleep(1)
        led.off()
        time.sleep(1)
    else:
        led.off()
        break


wlan = network.WLAN(network.STA_IF)
wlan.active(True)


while wlan.isconnected() != True and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
    wlan.connect('Wireless Network', 'The Password')

"""
def getTime(): 
    req_json = urequests.get('http://worldtimeapi.org/api/timezone/Europe/Berlin').json()
    return req_json['datetime'].split('T')[1].split('.')[0]



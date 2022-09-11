# This file is executed on every boot
#import gc

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
        print("AP turned off ...")
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect("ssid", "pswd")  # <<< FIXME
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

print("Starting network ...")
do_connect()
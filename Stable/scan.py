from bluepy import btle
from time import sleep
'''
scanner = Scanner()
devices = scanner.scan(5.0)
for device in devices:
    #print(device.getScanData())
    for (adtype,desc,value) in device.getScanData():
        if value == "YNC Laundry 1\r\n":
            global l1_addr
            l1_addr = device.addr
            print('l1_addr is %s' %l1_addr)
'''
cendana_addr = ["ec:24:b8:23:78:29","58:7A:62:17:B8:07"]

while True:
    i=0
    try:
        for addr_i in cendana_addr:
            global i
            i = i+1
            conn = btle.Peripheral()
#print(conn.readCharacteristic(0x0064))
            data = conn.readCharacteristic(0x0025)
            print(data.decode('utf8'))
            conn.disconnect()
    except Exception as e:
        pass
    sleep(0.5)

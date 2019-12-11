from bluepy import btle
import struct

class MyDel(btle.DefaultDelegate):
    def __init__(self,params):
        btle.DefaultDelegate.__init__(self)
    def handleNotification(self,cHandle,data):
        print("Handling notification...")
        print(data.decode('utf8'))
        
print("Connecting...")
p = btle.Peripheral("50:51:a9:fd:a6:f1")
p.setDelegate(MyDel(0))

while True:
    if p.waitForNotifications(1.0):
        continue
    print("Waiting")

'''print("Services...")
for svc in dev.services:
    print(str(svc))
'''    
    
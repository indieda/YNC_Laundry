from bluepy import btle
from time import sleep
from func_timeout import func_timeout, FunctionTimedOut
import time
import threading

url = 'http://webhook.site/9bc8eff7-fde0-4ffd-8e70-dfb12d85efae'

cendana_addr = ["ec:24:b8:23:78:29","58:7A:62:17:B8:07"]
washer_state_array = ["nil","nil"]
college = "Cendana"

def read_ble(ble_no,i):
    conn = btle.Peripheral(ble_no)
    data = conn.readCharacteristic(0x0025)
    data_decode = data.decode('utf8')
    print(data.decode('utf8')+str(i))
    conn.disconnect()
    read_ble.data_decode = data_decode

global i
i=0

def upload_to_web():
    try:
        t = threading.Timer(5.0,upload_to_web)
        t.daemon = True
        t.start()
        print(washer_state_array)
        for idx,d in enumerate(washer_state_array,start=1):
            if d == "on" :
            #idx = data_decoded[1]
                #response = requests.post(url , json = {'Washer {}'.format(d):'On'})
                print('Washer {}'.format(idx), d ,"and Uploaded")
                elif d == "off" :
                #idx = data_decoded[1]
                response = requests.post(url, json = {'Washer {}'.format(idx):'Off'})
                print('Washer {}'.format(idx), d ,"and Uploaded")
            elif d == "error" :
                response = requests.post(url, json = {'Washer {}'.format(idx):'Error'})
                print('Washer {}'.format(idx), d ,"and Uploaded")
            else:
                pass
    except Exception as e:
        print(e)
        pass
upload_to_web()

while True:
    i=0
    try:
        for addr_i in cendana_addr:
            func_timeout(0.8,read_ble,args=(addr_i,i))
            washer_state_array[i]=read_ble.data_decode
            #upload = threading.Thread(target=stdhandle, args = (read_ble.data_decode,i), daemon = True)
            i = i+1
    except Exception as e:
        #print(e)
        pass
    except FunctionTimedOut as e:
        #print(e)
        continue
    sleep(0.5)
    

'''from bluepy.btle import DefaultDelegate
class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        
    def handleNotification(self,hnd,data):
    
conn = Peripheral(addr)
print conn.readCharacteristic(0x0025)
'''

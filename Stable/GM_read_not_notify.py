from bluepy import btle
from time import sleep
from func_timeout import func_timeout, FunctionTimedOut
import time
import threading
import datetime
import requests

url = "https://webhook.site/a03ad0ea-9a75-4928-bad7-e0cae58a3709"
#https://webhook.site/#!/a03ad0ea-9a75-4928-bad7-e0cae58a3709/a5e58475-531e-4a0f-bc84-7bd0882c79ef/1
cendana_addr = ["ec:24:b8:23:78:29","58:7A:62:17:B8:07"]
washer_state_array = ["nil","nil"]
college = "Cendana"

time_prev = time.time()
time_elapsed = time.time() - time_prev
kill = [0,0]

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
        #t = threading.Timer(180.0,upload_to_web)
        #t.daemon = True
        #t.start()
        print(washer_state_array)
        for idx,d in enumerate(washer_state_array,start=1):
            if d == "on" :
            #idx = data_decoded[1]
                response = requests.post(url , json = {'Washer {}'.format(idx):'On'})
                print('Washer {}'.format(idx), d ,"and Uploaded")
            elif d == "off" :
                #idx = data_decoded[1]
                response = requests.post(url, json = {'Washer {}'.format(idx):'Off'})
                print('Washer {}'.format(idx), d ,"and Uploaded")
            elif d == "error" :
                response = requests.post(url, json = {'Washer {}'.format(idx):'Error'})
                print('Washer {}'.format(idx), d ,"and Uploaded")
            else:
                response = requests.post(url,json={"Washer {}".format(idx):"Couldn't read..."})
                kill[idx-1] = kill[idx-1] + 1
                pass
    except Exception as e:
        print(e)
        pass

while True:
    i=0
    try:
        for addr_i in cendana_addr:
            func_timeout(1.5,read_ble,args=(addr_i,i))
            washer_state_array[i]=read_ble.data_decode
            #upload = threading.Thread(target=stdhandle, args = (read_ble.data_decode,i), daemon = True)
            i = i+1
            time_elapsed = time.time() - time_prev
            if kill[i] > 3:
                os.system("rfkill block bluetooth")
                time.sleep(2.0)
                os.system("rfkill unblock bluetooth")
                time.sleep(2.0)
                print("Restarted bluetooth")
                kill = [0,0]
            if (time_elapsed > 180):
                upload_to_web()
                time_prev = time.time()
    except Exception as e:
        #print(e)
        pass
    except FunctionTimedOut as e:
        #print(e)
        continue
    sleep(0.5)

try:
        for addr_i in cendana_addr:
            try:
                func_timeout(0.9,read_ble,args=(addr_i,i))
                washer_state_array[i]=read_ble.data_decode
            #upload = threading.Thread(target=stdhandle, args = (read_ble.data_decode,i), daemon = True)
            except Exception as e:
                print(e)
                pass
            except FunctionTimedOut as e:
                print(e)
                pass
            time_elapsed = time.time() - time_prev
            if kill[i] > 3:
                os.system("rfkill block bluetooth")
                time.sleep(2.0)
                os.system("rfkill unblock bluetooth")
                time.sleep(2.0)
                print("Restarted bluetooth")
                kill = [0,0]
            if (time_elapsed > 180):
                upload_to_web()
                time_prev = time.time()
            i = i+1
            sleep(1.0)
    except:
        pass

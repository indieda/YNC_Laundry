#! /usr/bin/python3
from bluepy import btle
from time import sleep
from func_timeout import func_timeout, FunctionTimedOut
import time
import threading
import datetime, requests, os, sys, logging

url = "https://enrixpn98m8gp.x.pipedream.net"
#"https://webhook.site/d9cae541-78e7-48de-8791-79d8eccf84d7"
#19th Jan https://webhook.site/#!/a03ad0ea-9a75-4928-bad7-e0cae58a3709/a5e58475-531e-4a0f-bc84-7bd0882c79ef/1
#20th Jan https://webhook.site/#!/d9cae541-78e7-48de-8791-79d8eccf84d7/7ed9cfff-c943-4f45-9166-1f33090c9fb1/1
cendana_addr = ["ec:24:b8:23:78:29","58:7A:62:17:B8:07"]
washer_state_array = ["nil","nil"]
college = "Cendana"

time_prev = time.time()
time_exit = time.time()
time_elapsed = time.time() - time_prev
#kill = [0,0]

def read_ble(ble_no,i):
    try:
        conn = btle.Peripheral(ble_no)
        data = conn.readCharacteristic(0x0025)
        read_ble.data_decode = data.decode('utf8')
    #print(data.decode('utf8')+str(i))
        conn.disconnect()
        #read_ble.data_decode = data_decode
    except Exception as e:
        conn.disconnect()
        pass

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
                #response = requests.post(url,json={"Washer {}".format(idx):"Couldn't read..."})
                #kill[idx-1] = kill[idx-1] + 1
                pass
            washer_state_array[idx-1] = "nil"
    except Exception as e:
        print(e)
        pass


os.system("rfkill block bluetooth")
time.sleep(2.0)
os.system("rfkill unblock bluetooth")
time.sleep(2.0)
print("Restarted bluetooth")

print("Starting infinite loop")
while (time.time() - time_exit < 1165):
    i=0
    try:
        for addr_i in cendana_addr:
            try:
                func_timeout(0.8,read_ble,args=(addr_i,i))
                if (read_ble.data_decode == "on") or (read_ble.data_decode == "off") or (read_ble.data_decode == "error"):
                    washer_state_array[i]=read_ble.data_decode
                    print(read_ble.data_decode+str(i))
                    print(datetime.datetime.now())
                else:
                    pass
            #upload = threading.Thread(target=stdhandle, args = (read_ble.data_decode,i), daemon = True)
            except Exception as e:
                #print(e)
                pass
            except FunctionTimedOut as e:
                #print(e)
                pass
            time_elapsed = time.time() - time_prev

            #if kill[i] > 30:
                #kill = [0,0]
                #print("restarting program")
                #os.fsync(fd)
                #os.execv(__file__, sys.argv)
            if (time_elapsed > 8):
                upload_to_web()
                time_prev = time.time()
            i = i+1
            sleep(0.8)
    except Exception as e:
        #print(e)
        pass

exit()

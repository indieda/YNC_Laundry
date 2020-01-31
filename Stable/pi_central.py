#! /usr/bin/python3
from bluepy import btle
from time import sleep
from func_timeout import func_timeout, FunctionTimedOut
import time
import threading
import datetime, requests, os, sys, logging

ync_url="https://fb63a24c.ngrok.io"
url = "https://enrixpn98m8gp.x.pipedream.net"
#"https://webhook.site/d9cae541-78e7-48de-8791-79d8eccf84d7"
#19th Jan https://webhook.site/#!/a03ad0ea-9a75-4928-bad7-e0cae58a3709/a5e58475-531e-4a0f-bc84-7bd0882c79ef/1
#20th Jan https://webhook.site/#!/d9cae541-78e7-48de-8791-79d8eccf84d7/7ed9cfff-c943-4f45-9166-1f33090c9fb1/1
cendana_addr = ['ec:24:b8:23:78:29','58:7A:62:17:B8:07']
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
        #conn.disconnect()
        read_ble.data_decode = "nil"
        pass

global i
i=0

def write_log(message):
    f=open("log.txt","a")
    t=datetime.now()
    f.write("Time of event: ",t," Message: ", message,"\n")
    f.close()

def upload_to_web():
    try:
        #t = threading.Timer(180.0,upload_to_web)
        #t.daemon = True
        #t.start()
        global washer_state_array
        print(washer_state_array)
        for idx,d in enumerate(washer_state_array,0):
            if d == "on" :
            #idx = data_decoded[1]
                response = requests.post(url , json = {'Washer 6':'On, not available to use'})
                #response2 = requests.post(ync_url , json = {'Washer 6':'On'})
                write_log("Washer 6 On")
                print('Washer {}'.format(idx), d ,"and Uploaded")
            elif d == "off" :
                #idx = data_decoded[1]
                response = requests.post(url, json = {'Washer 6':'Off, available to use'})
                write_log("Washer 6 Off")
                #response2 = requests.post(ync_url , json = {'Washer 6':'Off'})
                print('Washer {}'.format(idx), d ,"and Uploaded")
            elif d == "error" :
                response = requests.post(url, json = {'Washer 6':'Error, the lock light is blinking!'})
                #response2 = requests.post(ync_url , json = {'Washer 6':'Error'})
                write_log("Washer 6 Error")
                print('Washer {}'.format(idx), d ,"and Uploaded")
            elif ((d == "first") or (d == "second") or (d == "third") or (d == "fourth") or (d == "fifth")  or (d == "sixth")  or (d == "seventh")  or (d == "eigth")  or (d == "ninth")  or (d == "tenth")  or (d == "max")):
                response = requests.post(url,json={"Washer {} ble message: {}".format(idx,d):"Lightval"})
            else:
                #response = requests.post(url,json={"Washer {} ble message: {}".format(idx,d):"Couldn't read..."})
                #kill[idx-1] = kill[idx-1] + 1
                pass
            washer_state_array[idx-1] = "nil"
    except Exception as e:
        #print(e)
        pass


os.system("rfkill block bluetooth")
time.sleep(2.0)
os.system("rfkill unblock bluetooth")
time.sleep(2.0)
print("Restarted bluetooth")
print("Starting infinite loop")

while (time.time() - time_exit < 580):
    i=0
    try:
        for addr_i in cendana_addr:
            try:
                func_timeout(0.8,read_ble,args=(addr_i,i))
                if ((read_ble.data_decode == "on") or (read_ble.data_decode == "off") or (read_ble.data_decode == "error") or (read_ble.data_decode == "first") or (read_ble.data_decode == "second") or (read_ble.data_decode == "third") or (read_ble.data_decode == "fourth")or (read_ble.data_decode == "fifth") or (read_ble.data_decode == "sixth") or (read_ble.data_decode == "seventh") or (read_ble.data_decode == "eigth") or (read_ble.data_decode == "ninth") or (read_ble.data_decode == "tenth") or (read_ble.data_decode == "max")):
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

#Referenced from: https://raspberrypi.stackexchange.com/questions/96247/are-there-reliable-methods-for-connecting-reconnecting-to-multiple-bluetooth-le
#The person added the sleep function.
#indieda added POST functionality, and restart bluetooth when there is prolonged silence from either devices.

from bluepy import btle
import struct, os
from concurrent import futures
import time
import datetime
import requests
global time_prev
global time_elapsed

time_prev = time.time()
time_elapsed = time.time() - time_prev
addr_var = ['50:51:a9:fd:a6:f1','50:51:A9:FD:A6:B2']
url = 'http://webhook.site/9bc8eff7-fde0-4ffd-8e70-dfb12d85efae'

def stdhandle(data_decoded):
    global time_prev
    time_prev = time.time()
    print(datetime.datetime.now())
    if data_decoded[0] == "l" :
        idx = data_decoded[1]
        response = requests.post(url , json = {'Washer {}'.format(idx):'Bright'})
        print('Washer {}'.format(idx), "Bright and Uploaded")
        return
    elif data_decoded[0] == "d" :
        idx = data_decoded[1]
        response = requests.post(url, json = {'Washer {}'.format(idx):'Dark'})
        print('Washer {}'.format(idx), "Dark and Uploaded")
        return
    elif data_decoded[0] == "b" :
        idx = data_decoded[1]
        response = requests.post(url, json = {'Washer {}'.format(idx):'Blinking'})
        print('Washer {}'.format(idx), "Blinking and Uploaded")
        return

class MyDelegate(btle.DefaultDelegate):

    def __init__(self,params):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self,cHandle,data):
        global addr_var
        global delegate_global
        print('got data: ', data)
        try:
#            datau= data
            data_decoded = data.decode('utf8')
            print(data_decoded)
            stdhandle(data_decoded)
            #            data_unpacked = struct.unpack("b",datau)
#            print(data_unpacked)
        except:
            pass

def perif_wait(perif):
    try:
#waitForNotifications will return a true or False. True only if HandleNotif was called. False if nothing.
        if (perif.waitForNotifications(1.0)):
#            print("waiting for notifications...")
            pass
    except Exception as e:
        pass
    finally:
#        print('disconnecting...')
        try:
            perif.disconnect()
            time.sleep(3.0)
        except Exception as e:
            print('failed to disconnect!', e)
            pass

def establish_connection(addr):
#    p = btle.Peripheral(addr)
#    p.disconnect()
#    time.sleep(2.0)
    while True:
        global t_elapsed
        global time_prev
        try:
#            print("Attempting to read from "+addr)
            p = btle.Peripheral(addr)
            p_delegate = MyDelegate(addr)
            p.withDelegate(p_delegate)
#            print("Connected to "+addr)
            perif_wait(p)
        except Exception as e:
            print("failed to connect to "+addr, e)
            time.sleep(2.0)
            continue
        finally:
            time_elapsed = time.time() - time_prev
            if time_elapsed > 180:
                os.system("rfkill block bluetooth")
                time.sleep(5.0)
                os.system("rfkill unblock bluetooth")
                time.sleep(5.0)
                pass

#os.popen('sudo hciconfig hci0 reset')
#os.popen('sudo invoke-rc.d bluetooth restart')
os.system("rfkill block bluetooth")
time.sleep(5.0)
os.system("rfkill unblock bluetooth")
time.sleep(5.0)
print("restarted bl")
ex = futures.ProcessPoolExecutor(max_workers = os.cpu_count())
results = ex.map(establish_connection,addr_var)

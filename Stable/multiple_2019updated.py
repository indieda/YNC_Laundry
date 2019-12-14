#Taken from this site: https://raspberrypi.stackexchange.com/questions/96247/are-there-reliable-methods-for-connecting-reconnecting-to-multiple-bluetooth-le
#The person added the sleep function.
#hrm

from bluepy import btle
import struct, os
from concurrent import futures
import time
import datetime

addr_var = ['50:51:a9:fd:a6:f1','50:51:A9:FD:A6:B2']

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
#            data_unpacked = struct.unpack("b",datau)
            print(data_decoded)
#            print(data_unpacked)
            print(datetime.datetime.now())
            return
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
            time.sleep(1.0)
        except Exception as e:
            print('failed to disconnect!', e)
            pass

def establish_connection(addr):
#    p = btle.Peripheral(addr)
#    p.disconnect()
#    time.sleep(2.0)
    while True:
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
#os.popen('sudo hciconfig hci0 reset')
#os.popen('sudo invoke-rc.d bluetooth restart')
os.system("rfkill block bluetooth")
time.sleep(5.0)
os.system("rfkill unblock bluetooth")
time.sleep(5.0)
print("restarted bl")
ex = futures.ProcessPoolExecutor(max_workers = os.cpu_count())
results = ex.map(establish_connection,addr_var)

#Taken from this site: https://raspberrypi.stackexchange.com/questions/96247/are-there-reliable-methods-for-connecting-reconnecting-to-multiple-bluetooth-le
#The person added the sleep function.

from bluepy import btle
import struct, os
from concurrent import futures
import time

addr_var = ['d8:a9:8b:b0:d0:49', 'd8:a9:8b:b0:da:dd']

class MyDelegate(btle.DefaultDelegate):

    def __init__(self,params):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self,cHandle,data):
        global addr_var
        global delegate_global
        print('got data: ', data)
        try:
            data_decoded = struct.unpack("b",data)
            print(data_decoded)
            return
        except:
            pass

def perif_wait(perif):
     try:
#waitForNotifications will return a true or False. True only if HandleNotif was called. False if nothing.
        if perif.waitForNotifications(8.0):
            print("waiting for notifications...")
     except Exception as e:
        pass
     finally:
        print('disconnecting...')
        try:
#            perif.disconnect()
            print("trying not to disconnect")
            time.sleep(4.0)
        except Exception as e:
            print('failed to disconnect!', e)
            pass

def establish_connection(addr):
    p = btle.Peripheral(addr)
    p_delegate = MyDelegate(addr)

    while True:
        try:
            print("Attempting to read from "+addr)
            p.withDelegate(p_delegate)
            print("Connected to "+addr)
            perif_wait(p)
        except Exception as e:
            print("failed to connect to "+addr, e)
            time.sleep(2.0)
            continue
ex = futures.ProcessPoolExecutor(max_workers = os.cpu_count())
results = ex.map(establish_connection,addr_var)
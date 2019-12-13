from bluepy import btle
import struct, os
from concurrent import futures
import datetime
from time import sleep

global addr_var
global delegate_global
global perif_global

addr_var = ['00:15:f4:34:a5:4b','d6:58:12:5b:00:0g']

class MyDelegate(btle.DefaultDelegate):

    def __init__(self,params):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self,cHandle,data):
        global addr_var
        global delegate_global

        for ii in range(len(addr_var)):
            if delegate_global[ii]==self:
                try:
                    data_decoded = struct.unpack("b",data)
                    perif_global[ii].writeCharacteristic(cHandle,struct.pack("b",55))
                    print("Address: "+addr_var[ii])
                    print(data_decoded)
                    return
                except:                    
                    pass
                try:
                    data_decoded = data.decode('utf-8')
                    perif_global[ii].writeCharacteristic(cHandle,struct.pack("b",55))
                    print("Address: "+addr_var[ii])
                    print(data_decoded)
                    return
                except:
                    return


def perif_loop(perif,indx):
    while True:
        try:
            if perif.waitForNotifications(1.0):
                print("waiting for notifications...")
                continue
        except:
            try:
                perif.disconnect()
                print("disconnecting perif: "+perif.addr+", index: "+str(indx))
                sleep(5)
                reestablish_connection(perif,perif.addr,indx)
            except:
                print("neither waiting for notifications (connected) nor able to disconnect")
                pass

delegate_global = []
perif_global = []
[delegate_global.append(0) for ii in range(len(addr_var))]
[perif_global.append(0) for ii in range(len(addr_var))]

def reestablish_connection(perif,addr,indx):
    while True:
        try:
            print("trying to reconnect with "+addr)
            perif.connect(addr)
            print("re-connected to "+addr+", index = "+str(indx))
            return
        except:
            continue

def establish_connection(addr):
    global delegate_global
    global perif_global
    global addr_var

    try:
        for jj in range(len(addr_var)):
            if addr_var[jj]==addr:
                print("Attempting to connect with "+addr+" at index: "+str(jj))
                p = btle.Peripheral(addr)
                perif_global[jj] = p
                p_delegate = MyDelegate(addr)
                delegate_global[jj] = p_delegate
                p.withDelegate(p_delegate)
                print("Connected to "+addr+" at index: "+str(jj))                    
                perif_loop(p,jj)
    except:
        print("failed to connect to "+addr)


ex = futures.ProcessPoolExecutor(max_workers = os.cpu_count())
results = ex.map(establish_connection,addr_var)
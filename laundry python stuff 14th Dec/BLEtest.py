#import pygatt

#adapter=pygatt.BGAPIBackend()

#adapter._detect_device_port()

from bluepy.btle import Scanner, DefaultDelegate, Peripheral
    import threading

    class NotificationDelegate(DefaultDelegate):

    def __init__(self, number):
        DefaultDelegate.__init__(self)
        self.number = number

    def handleNotification(self, cHandle, data):
        print 'Notification:\nConnection:'+str(self.number)+ \nHandler:'+str(cHandle)+'\nMsg:'+data

    bt_addrs = ['00:15:83:00:45:98', '00:15:83:00:86:72']
    connections = []
    connection_threads = []
    scanner = Scanner(0)

    class ConnectionHandlerThread (threading.Thread):
        def __init__(self, connection_index):
            threading.Thread.__init__(self)
            self.connection_index = connection_index

        def run(self):
            connection = connections[self.connection_index]
            connection.setDelegate(NotificationDelegate(self.connection_index))
            while True:
                if connection.waitForNotifications(1):
                    connection.writeCharacteristic(37, 'Thank you for the notification!')

    while True:
        print'Connected: '+str(len(connection_threads))
        print 'Scanning...'
        devices = scanner.scan(2)
        for d in devices:
            print(d.addr)
            if d.addr in bt_addrs:
                p = Peripheral(d)
                connections.append(p)
                t = ConnectionHandlerThread(len(connections)-1)
                t.start()
                connection_threads.append(t)
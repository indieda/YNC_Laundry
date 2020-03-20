import json
#This comes from the python status_db
from datetime import datetime

#constants
t = datetime.strptime("Sunday, 11:56:57 PM, 23-Feb-2001", '%A, %I:%M:%S %p, %d-%b-%Y')
s = "yea"

path = "./status_db.json"
with open(path) as db: 
    db = json.load(db)

def find_status(db, college, washer):
    t=0
    #state is "AVAILABLE OR UNAVAILABLE OR ERROR"
    for state in db[college][washer]:
        if int(db[college][washer][state]) > t:
            t = int(db[college][washer][state])
            s = state
    print(str(t)+s)

def find_latest(db, college, washer):
    #state is "AVAILABLE OR UNAVAILABLE OR ERROR"
    global t, s
    for state in db[college][washer]:
        if datetime.strptime(db[college][washer][state], '%A, %I:%M:%S %p, %d-%b-%Y') >= t:
            #t = datetime.strptime(db[college][washer][state], '%I:%M:%S %p %d/%H/%Y')
            time = db[college][washer][state]
            print(time)
            s = state
        else:
            pass
    find_latest.status = s
    find_latest.time = time

def update_status_ram(db, college, washer, status, time):
    db[college][washer][status] = time
    json_data = json.dumps(db)
    print(db)

#Method 1: fast method, just references what's on ram and paste
def update_status_hdd(filename=path):
    with open(filename,'w') as f: 
        json.dump(db, f, indent=4) 

#Method 2: slow method, extract out and edit and paste back.
"""
def update_status_hdd(college,washer,status,time, filename=path):
    with open(path) as json_file: 
        json_full = json.load(json_file) 
        temp = json_full[college][washer]
             #python object to be appended 
        y = {status:time}
            # appending data  
        temp.update(y)
    with open(filename,'w') as f: 
        json.dump(db, f, indent=4) 
"""



#update_status_ram(db,"Cendana", "Washer 1", "AVAILABLE", "8800")
#update_status_hdd()
#find_latest(db,"Cendana",'Washer_1')
#print(find_latest.status, find_latest.time)

#slow method command:
#update_status_hdd("Cendana", "Washer 1", "AVAILABLE", "100")

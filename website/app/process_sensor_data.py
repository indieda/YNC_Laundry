#from app import app
from datetime import datetime, timedelta, timezone
import json
import time
#constants
path = "/home/yun_da_legacy_hotmail_com/YNCLaundryViewer-/app/status_db.json"
#path = "./status_db.json"
ON = "UNAVAILABLE"
OFF = "AVAILABLE"
ERROR = "ERROR"
#with automatically closes files. So try without with.

#db = open(path, "r+")
#db = json.load(db)
#constants

def find_latest(db, college, washer):
    #state is "AVAILABLE OR UNAVAILABLE OR ERROR"
    t = datetime.strptime("Sunday, 11:56:57 PM, 23-Feb-2001", '%A, %I:%M:%S %p, %d-%b-%Y')
    s = "yea"
    for state in db[college][washer]:
        if datetime.strptime(db[college][washer][state], '%A, %I:%M:%S %p, %d-%b-%Y') >= t:
            #t = datetime.strptime(db[college][washer][state], '%I:%M:%S %p %d/%H/%Y')
            t = datetime.strptime(db[college][washer][state], '%A, %I:%M:%S %p, %d-%b-%Y')
            s = state
            time = datetime.strftime(t, '%A, %I:%M:%S %p, %d-%b-%Y')
    return s +" since: "+ time
    #find_latest.status = s
    #find_latest.time = time

#Method 1: fast method, just references what's on ram and paste
def update_status_hdd(db,filename=path):
    with open(filename,'w+') as f:
        json.dump(db, f, indent=4)


def update_status_ram(college, washer, status, time):
    #global db
    with open(path, "r+") as db: 
        db = json.load(db)
    db[college][washer][status] = time
    #json_data = json.dumps(tempjson)
    update_status_hdd(db)
    #with open(path) as db: 
    #    db = json.load(db)

def determine_sensor_status(value):
    if value < 300:
        return ON
    # elif value > 800:
    elif value >= 300 and value <= 1100:
        return OFF
    else:
        return ERROR

college_washer_set = {
    "Cendana": {
        "Washer_1": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_2": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_3": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_4": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_5": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_6": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        }
    },
    "Elm": {
        "Washer_1": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_2": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_3": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_4": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_5": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_6": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        }
    },
    "Saga": {
        "Washer_1": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_2": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_3": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_4": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_5": {
            "AVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Wednesday, 11:59:59 PM, 01-Jan-2020"
        },
        "Washer_6": {
            "AVAILABLE": "Monday, 01:48:26 AM, 24-Feb-2020",
            "UNAVAILABLE": "Wednesday, 11:59:59 PM, 01-Jan-2020",
            "ERROR": "Monday, 01:13:53 AM, 24-Feb-2020"
        }
    }
}

#note, washer and machineLabel are the same things
def get_latest_sensor_value(college, machineLabel):
    #with open(path) as db: 
    #    college_washer_set[college][machineLabel] = json.load(db)
    ss = ""
    with open(path, "r+") as db: 
        db = json.load(db)
    try:
        #print(college_washer_set[college][machineLabel])
        ss = find_latest(db,college,machineLabel)
        #Adding sleep here makes it worse, I think it's becaue of the async funcion of javascript.
        #time.sleep(1)
        #ss = find_latest.status + "\n" + find_latest.time
        return ss
    except Exception as e:
        print(e)
        pass
#sanity check
#update_status_ram("Saga", "Washer_6", "AVAILABLE", datetime.strftime(datetime.now(), "%A, %I:%M:%S %p, %d-%b-%Y"))
#print(get_latest_sensor_value("Saga","Washer_6"))

print(repr(get_latest_sensor_value("Elm","Washer_6")))
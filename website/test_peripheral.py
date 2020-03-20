from datetime import datetime, timedelta, timezone
import json
from test import find_latest, db, update_status_ram, update_status_hdd

update_status_ram(db,"Saga", "Washer_6", "AVAILABLE", datetime.strftime(datetime.now(), "%A, %I:%M:%S %p, %d-%b-%Y"))
update_status_hdd()
find_latest(db,"Cendana",'Washer_1')
print( find_latest.status + "\n" + find_latest.time)
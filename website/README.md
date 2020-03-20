# YNCLaundryViewer-

Yale-NUS Laundry Viewer Platform





Failed stuff:
#Script to generate database in case of corruption
db = {"Cendana":"_"}
for x in colleges:
    db.update({x:"_"})
for x in colleges:
    total = {}
    for y in sixes:
        total.update({"Washer_{}".format(y):"_"})
    db.update({x:total})

for x in colleges:
    total = {}
    last = {}
    for y in sixes:
        stotal = {}
        for z in statuses:
            stotal.update({z:tt})
        total.update({"Washer_{}".format(y):stotal})
    db.update({x:total})


"""
for z in statuses:
    for y in sixes:
        db[college][washer] = x
        for x in colleges:
            db[college] = x
#update_status_ram(db, x , "Washer_{}".format(y), z, tt)
"""

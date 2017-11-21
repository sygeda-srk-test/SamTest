#!/usr/bin/python
import sys
import time
#import tdb

while 1 == 1:
#db = tdb.open(sys.argv[1])
    db = {}
    h = c = 0


    for key in db:
        if key[0:4] == 'pppd':
            ls = db[key].split(";")
        if len(ls) < 8:
            h = h+1
        else:
            c = c+1

    sys.stdout.write("\rhalted %4d, connected %4d" % (h, c))

    sys.stdout.flush()

#db.close()
    time.sleep(3)


abc()
def()

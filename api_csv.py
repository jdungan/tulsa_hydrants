import sys
import hashlib
import os
import time

import requests
import ujson
import csv
from csv import DictWriter

hydrant_request ={
  "near":  "36.1539,-95.99252,40mi",
  "sets":"hydrants",
  "limit":50,
  "offset":0,
}

def getHydrants(offset):
    hydrant_request['offset']=offset
    r=requests.get("http://oklahomadata.org/boundary/1.0/point/",params=hydrant_request)
    u=ujson.loads(r.text)
    recvd=str(len(u['objects']))
    sys.stdout.write(str(offset))
    return u['objects']
    
hydrants_received=50




startnum=0
header_written = False

the_file=open('hydrants.csv','w')


while hydrants_received == 50:
# while startnum < 200:    
    hydrants=getHydrants(startnum)
    hydrants_received= len(hydrants)
    
    
    for hydrant in hydrants:
        sys.stdout.write('.')
        writer = DictWriter(the_file, hydrant['metadata'].keys())
        if header_written != True:
            writer.writeheader()
            header_written = True
        writer.writerow(hydrant['metadata'])

    startnum += 50 

the_file.close()

print "done"
    

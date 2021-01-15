# -*- coding: utf-8 -*-

import os
import datetime
import calendar
import requests
import json
import time


now = datetime.datetime.utcnow()
ten_minutes_ago = datetime.datetime.utcnow() - datetime.timedelta(minutes = 10)
filename = f"{ten_minutes_ago.strftime('%Y%m%d_%H%M%S'){i}_{now.strftime('%H%M%S')}"

sif_now = calendar.timegm(now.timetuple())
sif_last_hour = calendar.timegm(ten_minutes_ago.timetuple())

url = f"https://csp.infoblox.com/api/dnsdata/v1/dns_event?t0={sif_last_hour}&_format=json&t1={sif_now}&source=rpz"

time.sleep(120 )
payload = {}
headers = {
  'Authorization': 'Token <YOUR API KEY HERE>'
}
response = requests.request("GET", url, headers=headers, data = payload)

path = "/tmp/rpz"
if not os.path.exists(path):
    os.makedirs(path)

completeName = os.path.join(path, filename+".json")         
data = json.loads(response.content)
write_data = json.dumps(data)

fh = open(completeName, 'w') 
fh.write(write_data)
fh.close()

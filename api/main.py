import urllib.request ,urllib.error ,urllib.parse
import json

api_endpoint ="http://api.coindesk.com/v1/bpi/currentprice.json"
api_endpoint1 ="http://api.publicapis.org/entries"
api_endpoint2 ="http://api.open-notify.org/iss-now.json"

urlhandler = urllib.request.urlopen(api_endpoint2)
print(urlhandler)
data = urlhandler.read()
print(type(data))
try :
    js = json.loads(data)
except :
    js = None

print(type(js))
if not js or 'status' not in js or js['status'] != 'OK' :
    print("something went wrong")

data_js = json.dumps(js,indent=4)
print(type(data_js))
print(data_js)

iss_position = js["iss_position"]
print(iss_position)
longitude  = js["iss_position"]["longitude"]
print(longitude)
latitude = js["iss_position"]["latitude"]
print(latitude)
position = (longitude,latitude)
print(position)

exit()

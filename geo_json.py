import urllib
import json

api_url="http://maps.googleapis.com/maps/api/geocode/json?"

while(True):
    location=raw_input("enter location ")
    if(len(location)<1):
        break
    url=api_url+urllib.urlencode({'sensor':'false','address': location})
    print ("Retrieving",url)
    data=urllib.urlopen(url).read()
    try:
        js=json.loads(str(data))
    except:
        js=None
    if('status' not in js or js['status']!="OK"):
        print ("===== Failure loading====")
        continue
    print (json.dumps(js,indent=4))
    lat=js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    address=js["results"][0]["formatted_address"]
    print ("lat",lat,"lng",lng)
    print (js['results'][0]['formatted_address'])
    

"""
Location History.json is provided by google and is unique to your account
"""



import json
import time
import datetime
from geopy.geocoders import Nominatim
names = json.loads(open('Location History.json').read())
geolocator = Nominatim(user_agent="https://nominatim.openstreetmap.org/reverse")

json_obj = json.dumps(names)
json_size = len(json_obj)

def get_location(size):
    x = 0
    
    while json_size:

        latitude = names["locations"][x]["latitudeE7"]
        longitude = names["locations"][x]["longitudeE7"]
        latitude = latitude / 10000000
        longitude = longitude / 10000000
   
        secs = names["locations"][x]["timestampMs"]
        secs = int(secs)
        date = datetime.datetime.fromtimestamp(secs/1000.0)

        print(date)

        add = ' ' + str(latitude) + ', ' + str(longitude)

        location = geolocator.reverse(add)
        print(' latitude: ', latitude)
        print(' longitude: ', longitude)
        print(location.address)
        print(' ')

        x+= size
        time.sleep(2)

def main():
    size = int(input('Size: '))
    get_location(size)

main()
    
#print("latitude: " + location['latitudeE7'] +"/n longitude" +  location['longitudeE7'] )
#x= json.dump(names)
#print(x)



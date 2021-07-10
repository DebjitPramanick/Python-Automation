from geopy.geocoders import Nominatim
from geopy import distance

geocoder = Nominatim(user_agent="Dummy Agent")
location1 = "kolkata"
location2 = "mumbai"

crd1 = geocoder.geocode(location1)
crd2 = geocoder.geocode(location2)

print(crd1, crd2)

lat1,long1 = (crd1.latitude),(crd1.longitude)
lat2,long2 = (crd2.latitude),(crd2.longitude)

place1 = (lat1, long1)
place2 = (lat2, long2)

print(distance.distance(place1, place2))
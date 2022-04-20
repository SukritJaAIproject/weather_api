# print(len(data['observations']))
# print(data['observations'][2].keys())
# print(data['observations'][0]['metric'].keys())
# print(response.text)
# print(data.keys())
# print(data['observations'])
##################################
# print(data.keys())
# print(data['location'].keys())
# print('latitude: ', data['location']['latitude'])
# print('longitude: ', data['location']['longitude'])
# print('city: ', data['location']['city'])
# print('locale: ', data['location']['locale'])
# print('neighborhood: ', data['location']['neighborhood'])
# print('adminDistrict: ', data['location']['adminDistrict'])
# print('adminDistrictCode: ', data['location']['adminDistrictCode'])
# print('postalCode: ', data['location']['postalCode'])
# print('postalKey: ', data['location']['postalKey'])
# print('country: ', data['location']['country'])
# print('countryCode: ', data['location']['countryCode'])
# print('ianaTimeZone: ', data['location']['ianaTimeZone'])
# print('displayName: ', data['location']['displayName'])
# print('dstEnd: ', data['location']['dstEnd'])
# print('dstStart: ', data['location']['dstStart'])
# print('dmaCd: ', data['location']['dmaCd'])
# print('placeId: ', data['location']['placeId'])
# print('disputedArea: ', data['location']['disputedArea'])
# print('disputedCountries: ', data['location']['disputedCountries'])
# print('disputedCountryCodes: ', data['location']['disputedCountryCodes'])
# print('disputedCustomers: ', data['location']['disputedCustomers'])
# print('disputedShowCountry: ', data['location']['disputedShowCountry'])
# print('canonicalCityId: ', data['location']['canonicalCityId'])
# print('countyId: ', data['location']['countyId'])
# print('locId: ', data['location']['locId'])
# print('locationCategory: ', data['location']['locationCategory'])
# print('pollenId: ', data['location']['pollenId'])
# print('pwsId: ', data['location']['pwsId'])
# print('regionalSatellite: ', data['location']['regionalSatellite'])
# print('tideId: ', data['location']['tideId'])
# print('type: ', data['location']['type'])
# print('zoneId: ', data['location']['zoneId'])

##################################
# print(data['location'].keys())
# print('stationName: ', data['location']['stationName'])
# print('stationId: ', data['location']['stationId'])
# print('obsType: ', data['location']['obsType'])
# print('latitude: ', data['location']['latitude'])
# print('longitude: ', data['location']['longitude'])
# print('distanceKm: ', data['location']['distanceKm'])

# print(data.keys())
# print(data['location'])
# print(data['location'].keys())
# print(data['location']['adminDistrictCode'])
# print('stationName: ', data['location']['stationName'])
# print('countryCode: ', data['location']['countryCode'])
# print('stationId: ', data['location']['stationId'])
# print('ianaTimeZone: ', data['location']['ianaTimeZone'])
# print('obsType: ', data['location']['obsType'])
# print('latitude: ', data['location']['latitude'])
# print('longitude: ', data['location']['longitude'])
# print('distanceKm: ', data['location']['distanceKm'])
# print('distanceMi: ', data['location']['distanceMi'])

lat, lon, apiKey = 13.917, 100.600, "92034bae5e864c0a834bae5e86fc0a18"
url = "https://api.weather.com/v3/location/point?format=json&geocode="+str(lat)+","+str(lon)+"&language=en-US&apiKey="+str(apiKey)
payload, headers={}, {}
response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)

print(data.keys())
print(data['location'].keys())
print('latitude: ', data['location']['latitude'])
print('longitude: ', data['location']['longitude'])
print('city: ', data['location']['city'])
print('adminDistrict: ', data['location']['adminDistrict'])
print('placeId: ', data['location']['placeId'])
print('canonicalCityId: ', data['location']['canonicalCityId'])
print('locId: ', data['location']['locId'])
print('pwsId: ', data['location']['pwsId'])
print('regionalSatellite: ', data['location']['regionalSatellite'])

##### Search Observation by Geocode: #####
import time
import json
import datetime
import requests
import pandas as pd
from tqdm import tqdm
lat, lon, apiKey = 13.989478999999996, 100.616387, "92034bae5e864c0a834bae5e86fc0a18"
url = "https://api.weather.com/v3/location/near?geocode="+str(lat)+","+str(lon)+"&product=observation&format=json&apiKey="+str(apiKey)
payload, headers={}, {}
response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)

stationName, stationId, obsType = data['location']['stationName'], data['location']['stationId'], data['location']['obsType']
lat, lon, distanceKm = data['location']['latitude'], data['location']['longitude'], data['location']['distanceKm']
stationNames, stationIds, obsTypes, lats, lons, distanceKms = [], [], [], [], [], []

for i in range(len(stationName)):
  stationNames.append(stationName[i]); stationIds.append(stationId[i]);
  obsTypes.append(obsType[i])
  lats.append(lat[i]); lons.append(lon[i]); distanceKms.append(distanceKm[i]);
df = pd.DataFrame({'stationName':stationNames, 'stationId':stationIds, 'obsType':obsTypes, 'latitude':lats, 'longitude':lons, 'distanceKm':distanceKms})
df
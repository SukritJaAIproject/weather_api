import json
import tqdm
import requests
import pandas as pd
from statistics import mean

def location_near(lat_near, lon_near, apiKey):
  '''หา station ที่ใกล้กับ lat lon ที่ป้อน
  req param : lat lon
  res param : stationName, stationId, obsType, lat, lon, distanceKm
  '''
  url = "https://api.weather.com/v3/location/near?geocode="+str(lat_near)+","+str(lon_near)+"&product=observation&format=json&apiKey="+str(apiKey)
  payload, headers={}, {}
  response = requests.request("GET", url, headers=headers, data=payload)
  data = json.loads(response.text)
  stationName, stationId = data['location']['stationName'], data['location']['stationId']
  obsType, distanceKm = data['location']['obsType'], data['location']['distanceKm']
  lat, lon = data['location']['latitude'], data['location']['longitude']
  stationNames, stationIds, obsTypes, distanceKms, lats, lons = [], [], [],  [], [], []
  for i in range(len(stationName)):
    stationNames.append(stationName[i]); stationIds.append(stationId[i]); obsTypes.append(obsType[i]);
    lats.append(lat[i]); lons.append(lon[i]); distanceKms.append(distanceKm[i]);
  df = pd.DataFrame({'stationName':stationNames, 'stationId':stationIds, 'obsType':obsTypes, 'lat':lats, 'lon':lons, 'distanceKm':distanceKms})
  return df

def location_point(lat, lon, apiKey):
  '''หา pwsId  จาก lat lon ที่ป้อน
  req param : lat lon
  res param : lat, lon, city, pwsId
  '''
  url = "https://api.weather.com/v3/location/point?format=json&geocode="+str(lat)+","+str(lon)+"&language=en-US&apiKey="+str(apiKey)
  payload, headers={}, {}
  response = requests.request("GET", url, headers=headers, data=payload)
  data = json.loads(response.text)
  latitude, longitude =  data['location']['latitude'], data['location']['longitude']
  city, pwsId = data['location']['city'], data['location']['pwsId']
  return [latitude, longitude, city, pwsId]

def wunderground_current(lat, lon, apiKey):
  ''' location near -> location point -> current data
  req param : lat lon
  res param : lat, lon, mean temp, mean rh
  '''
  lat2, lon2, city2, pwsId2, stationId2, tempav, rhav  = [], [], [], [], [],[], []
  df1 = location_near(lat, lon, apiKey) ## location near
  for i in range(df1.shape[0]):
    try:
      lat, lon, stationId = df1['lat'][i], df1['lon'][i], df1['stationId'][i]
      info_list = location_point(lat, lon, apiKey) ## location point
      lat2.append(info_list[0]); lon2.append(info_list[1]);
      city2.append(info_list[2]); pwsId2.append(info_list[3]); stationId2.append(stationId);
    except:
      lat2.append(0); lon2.append(0);
      city2.append("None"); pwsId2.append("None"); stationId2.append("None");
  df2 = pd.DataFrame({'stationId':stationId2, 'lat':lat2, 'lon':lon2, 'city':city2,'pwsId':pwsId2})
  for stationId in df2['pwsId']:
    url = "https://api.weather.com/v2/pws/observations/current?stationId="+str(stationId)+"&format=json&units=m&apiKey="+str(apiKey)
    payload, headers={}, {}
    try:
      response = requests.request("GET", url, headers=headers, data=payload)
      data = json.loads(response.text)
      stationID = data['observations'][0]['stationID']
      obsTimeLocal, neighborhood = data['observations'][0]['obsTimeLocal'], data['observations'][0]['neighborhood']
      solarRadiation = data['observations'][0]['solarRadiation']
      lat, lon = data['observations'][0]['lat'], data['observations'][0]['lon']
      humidity, temp = data['observations'][0]['humidity'], data['observations'][0]['metric']['temp']
      #print(stationId, 'lat:', lat, 'lon:', lon,'temp:', temp, 'humidity:', humidity)
      tempav.append(temp); rhav.append(humidity); 
    except:
      pass
  return {'lat':lat, 'lon':lon, 'mean temp':mean(tempav), 'mean rh':mean(rhav)}
 
latlons = {'chula': (13.7389852,100.528069),  'chula_14z': (13.7389592,100.5274038),
           'ChangArena_z17': (14.9658694,103.0921753), 'Futurepark':(13.989478999999996, 100.616387 )}

# ChangArena_z17  
lat, lon, apiKey =  14.9658694, 103.0921753 , "92034bae5e864c0a834bae5e86fc0a18"
result = wunderground_current(lat, lon, apiKey)
print(result)
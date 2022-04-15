import json
import requests
import pandas as pd

def Nearby_Stations(lat, lon, api_key):
  '''
  10 Nearby Stations
  request param [lat, lon]
  response param [Id, Name, distance]
  '''
  url, querystring = "https://meteostat.p.rapidapi.com/stations/nearby", {"lat":lat,"lon":lon}
  headers = { "X-RapidAPI-Host": "meteostat.p.rapidapi.com", "X-RapidAPI-Key": api_key}
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = json.loads(response.text)
  ids, names, distances = [], [], []
  for i in range(len(data['data'])):
    # id, name, dis = data['data'][0]['id'], data['data'][0]['name']['en'], data['data'][0]['distance']/1000
    id, name = data['data'][i]['id'], data['data'][i]['name']['en']
    dis = data['data'][i]['distance']/1000
    ids.append(id)
    names.append(name)
    distances.append(dis)
  df = pd.DataFrame({'Id':ids, 'Name':names, 'distance(km)':distances})
  return df

lat, lon = 13.989478999999996, 100.616387
api_key = "a949fee7f6mshf15640e97c60b31p1a6549jsn36e6b0350757"
data = Nearby_Stations(lat, lon, api_key)
print(data)
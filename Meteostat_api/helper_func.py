#!pip install meteostat

import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from meteostat import Point, Daily, Hourly, Stations

def h_data_f_location(locationID, start, end):
  '''
  Historical data
  get hourly data from location Id
  request param [locationID, start, end]
  response param [time, temp	dwpt	rhum	prcp	snow	wdir	wspd	wpgt	pres	tsun	coco]
  '''
  data = Hourly(locationID, start, end) 
  data = data.fetch()
  data = data[['temp', 'dwpt', 'rhum', 'prcp', 'wdir', 'wspd', 'pres', 'coco']]
  return data

def d_data_f_latlon(lat, lon):
  '''
  Historical data
  get daily data
  request param [lat, lon , start, end]
  response param [date, tavg	tmin	tmax	prcp	snow	wdir	wspd	wpgt	pres	tsun]
  '''
  location = Point(lat, lon, 70)
  data = Daily(location, start, end)
  data = data.fetch()
  data = data[['tavg', 'tmin', 'tmax', 'prcp', 'wdir', 'wspd', 'pres']]
  return data

def closest_wstation(lat, lon, start, end, res):
  '''
  Get closest weather station to your location [daily, hourly]
  request param [lat, lon, start_date, end_date, res]
  response param ['name', 'latitude', 'longitude','distance']
  '''
  stations = Stations().nearby(lat, lon)
  if res == 'daily':
    stations = stations.inventory('daily', (start, end))
  else:
    stations = stations.inventory('hourly', (start, end))
  station = stations.fetch(1) ## Fetch closest station (limit = 1)
  station['id'] = station.index
  df = station[['id', 'name', 'wmo', 'icao', 'latitude', 'longitude', 'distance']]
  result = {'station_id':df['id'].values[0], 'station name':df['name'].values[0], 'lat':df['latitude'].values[0], 'lon':df['longitude'].values[0], 'distance':round(df['distance'].values[0]/1000,3)}
  return result

def dh_hist_f_station(station, start, end, res):
  '''
  Historical data
  Get Daily/Hourly data at the selected weather station
  request param [station_id, start, end, res]
  response param [time, temp, rhum]
  '''
  if res == 'daily':
    data = Daily(station, start, end)
  else:
    data = Hourly(station, start, end)
  data = data.fetch()
  df = data[['temp', 'rhum']]
  return df
  
################################ 
locationID = '72219'
lat, lon = 13.989478999999996, 100.616387
start, end, res = datetime(2021, 1, 1), datetime(2021, 1, 15), "hourly"
#start, end = datetime(2021, 1, 1), datetime(2021, 2, 28, 23, 59)

result1 = closest_wstation(lat, lon, start, end, res)
print(result1)

result2 = h_data_f_location(locationID, start, end)
print(result2)

result3 = d_data_f_latlon(lat, lon)
print(result3)

result4 = dh_hist_f_station(result1['station_id'], start, end, res)
print(result4)

# data.plot(y=['tavg', 'tmin', 'tmax'], kind = 'line')
# data.plot(y=['temp', 'rhum'], kind = 'line')
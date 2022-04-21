!pip install -q meteostat
!pip install -q wwo-hist
!pip install -q mercantile
!pip install -q pyGeoTile
!pip install -q pyowm

########### (lat, lon, z) -> (x, y, z) 
import pytz
import requests
import mercantile
import pandas as pd
import datetime
import json, time
from pygeotile.tile import Tile
from pygeotile.point import Point
from datetime import datetime, timedelta
#from google.colab.patches import cv2_imshow

## meteostat_api
from meteostat_api.helper_func import h_data_f_location, d_data_f_latlon, closest_wstation, dh_hist_f_station
from meteostat_api.nearby_station import Nearby_Stations
from meteostat_api.station_his_data import station_his_data
from meteostat_api.his_data_point import his_data_point, current_data_point
from meteostat_api.nearby_stations_get_data import nearby_stations_get_data

## Visualcrossing_api
from helper_func import *
## Visualcrossing_api
from Visualcrossing_api.Visualcross_hist import Visualcrossing_hist
from Visualcrossing_api.Visualcrossing_forecast import Visualcrossing_forecast

## wwo_api
from wwo_api.wwo_his_data import wwo_his_data
from wwo_api.wwo_by_date import wwo_by_date
from wwo_api.wwo_curr_data import wwo_curr_data
## wunderground_api
from wunderground_api.wunderground_current import wunderground_current
from wunderground_api.wg_his_data import wg_his_data
## openweather_api
from openweather_api.open_his_data import open_his_data
from openweather_api.open_his_data import current
from openweather_api.open_his_data import openweathermap_f
from openweather_api.open_his_data import *
## tmd_api
from tmd_api.current_tmd_data import current_tmd_data
from tmd_api.tmd_forecast import tmd_forecast

## 1 lat-lon point  -> 1 TMS -> lat-lon bboxes
## (lat_min, lon_min) : (q2), (lat_min, lon_max) : (q1)
## (lat_max, lon_min) : (q3) (lat_max, lon_max) : (q4)

lat, lon, zoom = 13.989478999999996, 100.616387, 14
cur_date = datetime.today().strftime("%Y-%m-%d")
cur_time = datetime.now(pytz.timezone('Asia/Bangkok')).strftime("%H:%M:%S")
apikey_met = "a949fee7f6mshf15640e97c60b31p1a6549jsn36e6b0350757"
appid_open = "283019a4b61eafae7824e4d94b8f1926" #thanksfordoo@gmail.com
apiKey_wdg = "92034bae5e864c0a834bae5e86fc0a18"

def weather_pred(lat, lon, zoom, cur_date, cur_time, appid_open, apikey_met):
  x, y, z = latlon2TMS(lat, lon, zoom)
  bbox_latlon = TMS2latlon_bound(x, y, z)
  lat_max, lon_min =  bbox_latlon[3], bbox_latlon[0]    #lat-north, #lon-west
  lat_min, lon_max  = bbox_latlon[1], bbox_latlon[2]    #lat-south, #lon-east
  
  ## openweather_api
  temp_q1_open, rh_q1_open = openweathermap_f(lat_min, lon_max, appid_open) #q1
  temp_q2_open, rh_q2_open = openweathermap_f(lat_min, lon_min, appid_open) #q2
  temp_q3_open, rh_q3_open = openweathermap_f(lat_max, lon_min, appid_open) #q3
  temp_q4_open, rh_q4_open = openweathermap_f(lat_max, lon_max, appid_open) #q4

  ## meteostat_api1
  temp_q1_m1, rh_q1_m1 = nearby_stations_get_data(lat_min, lon_max, apikey_met, cur_date, cur_time)['temp'], nearby_stations_get_data(lat_min, lon_max, apikey_met, cur_date, cur_time)['rh'] #q1
  temp_q2_m1, rh_q2_m1 = nearby_stations_get_data(lat_min, lon_min, apikey_met, cur_date, cur_time)['temp'], nearby_stations_get_data(lat_min, lon_max, apikey_met, cur_date, cur_time)['rh'] #q2
  temp_q3_m1, rh_q3_m1 = nearby_stations_get_data(lat_max, lon_min, apikey_met, cur_date, cur_time)['temp'], nearby_stations_get_data(lat_min, lon_max, apikey_met, cur_date, cur_time)['rh'] #q3
  temp_q4_m1, rh_q4_m1 = nearby_stations_get_data(lat_max, lon_max, apikey_met, cur_date, cur_time)['temp'], nearby_stations_get_data(lat_min, lon_max, apikey_met, cur_date, cur_time)['rh'] #q4

  ## meteostat_api2
  temp_q1_m2, rh_q1_m2 = current_data_point(lat_min, lon_max, cur_date, cur_date, apikey_met, cur_date, datetime.now().strftime("%H")) #q1
  temp_q2_m2, rh_q2_m2 = current_data_point(lat_min, lon_min, cur_date, cur_date, apikey_met, cur_date, datetime.now().strftime("%H")) #q2
  temp_q3_m2, rh_q3_m2 = current_data_point(lat_max, lon_min, cur_date, cur_date, apikey_met, cur_date, datetime.now().strftime("%H")) #q3
  temp_q4_m2, rh_q4_m2 = current_data_point(lat_max, lon_max, cur_date, cur_date, apikey_met, cur_date, datetime.now().strftime("%H")) #q4

  ## Calculate temp, rh
  E_temp_open = (temp_q1_open+temp_q2_open+temp_q3_open+temp_q4_open)/4
  E_rh_open =(rh_q1_open+rh_q2_open+rh_q3_open+rh_q4_open)/4
  print('openweather_api: ', 'Temp: ', E_temp_open, 'Rh: ',  E_temp_open)

  E_temp_m1 = (temp_q1_m1+temp_q2_m1+temp_q3_m1+temp_q4_m1)/4
  E_rh_m1 =(rh_q1_m1+rh_q2_m1+rh_q3_m1+rh_q4_m1)/4
  print('meteostat: ', 'Temp: ', E_temp_m1, 'Rh: ',  E_rh_m1)

  E_temp_m2 = (temp_q1_m2+temp_q2_m2+temp_q3_m2+temp_q4_m2)/4
  E_rh_m2 =(rh_q1_m2+rh_q2_m2+rh_q3_m2+rh_q4_m2)/4
  print('meteostat: ', 'Temp: ', E_temp_m2, 'Rh: ',  E_rh_m2)

  E_temp = np.array([E_temp_open, E_temp_m1, E_temp_m2]).mean()
  E_rh = np.array([E_rh_open, E_rh_m1, E_rh_m2]).mean()

  ## Actual station from wunderground
  actual = wunderground_current(lat, lon, apiKey_wdg)
  print('Actual', actual)

  # result = {'temp&rh_q1':[temp_q1 ,rh_q1], 'temp&rh_q2':[temp_q2 ,rh_q2], 'temp&rh_q3':[temp_q3 ,rh_q3], 'temp&rh_q4':[temp_q4 ,rh_q4], 'Estimate_temp&rh':[Estimate_temp, Estimate_rh], 'actual':actual}
  result = {'Estimate_temp&rh':[E_temp, E_rh], 'actual':actual}
  return result

result = weather_pred(lat, lon, zoom, cur_date, cur_time, appid_open, apikey_met)
print(result)
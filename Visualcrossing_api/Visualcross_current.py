import csv
import json
import sys
import codecs
import pandas as pd
import urllib.request
from datetime import datetime
from datetime import date
from google.colab import files

########## current data ##########
lat, lon = "13.989478999999996", "100.616387"

# api_key = "Q82HADKP8VA46L5QNL2LJLC4Y" #Chula
# api_key = "2DSCEBCSZCZ87NGFDKK3Z84GB" #KU
api_key = "9ECDU5PSBATV5BF3VYZH2MRU4" #Thanksfordoo

current_date = datetime.today().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")
print("current_date =", current_date, "Current Time =", current_time)

def Visualcross_current(lat, lon, api_key, current_date, current_time):
  url1 = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
  url2 = str(lat)+"%2C%20"+str(lon)+"/"+str(current_date)+"/"+str(current_date)
  url3 = "?unitGroup=metric&elements=datetime%2CdatetimeEpoch%2Cname%2Caddress%2CresolvedAddress%2Clatitude%2Clongitude%2Ctemp%2Chumidity%2Cstations%2Csource&include=obs%2Chours&key="
  url4 = str(api_key)+"&contentType=json"
  url = url1+url2+url3+url4
  try: 
    resp_text = urllib.request.urlopen(url).read().decode('UTF-8')
    jsonData = json.loads(resp_text)
  except urllib.error.HTTPError  as e:
    ErrorInfo= e.read().decode() 
    print('Error code: ', e.code, ErrorInfo)
    sys.exit()
  except  urllib.error.URLError as e:
    ErrorInfo= e.read().decode() 
    print('Error code: ', e.code,ErrorInfo)
    sys.exit()
  his_data = jsonData['days']
  dates, times, temps, rhs  = [], [],  [], []
  for i in range(len(his_data)):
    date, data = his_data[i]['datetime'], his_data[i]['hours']
    for j in range(len(data)):
      datetimes = data[j]['datetime']
      temp, rh = data[j]['temp'], data[j]['humidity']
      if datetimes[0:2] == current_time[0:2]:
        # print('datetime[0:2]', datetimes[0:2], 'current_time[0:2]', current_time[0:2])
        print('datetime: ', datetimes, 'current_time: ', current_time , 'Temp: ', temp, 'humidity: ', rh)
        result = {'datetime':datetimes, 'current_time':current_time , 'Temp':temp, 'humidity':rh}
  return result
result = Visualcross_current(lat, lon, api_key, current_date, current_time)
result
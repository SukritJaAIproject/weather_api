import csv
import json
import codecs
import urllib.request
import sys
import pandas as pd
from google.colab import files


def Visualcrossing_forecast(lat, lon, api_key):
  url1 = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
  url2 = str(lat)+"%2C%20"+str(lon)+"?unitGroup=metric&key="+str(api_key)+"&contentType=json"
  url = url1+url2
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

  date_list, datetime_list = [], []
  temp_list, rh_list = [], []

  for i in range(0,15):
    date, inday = jsonData['days'][i]['datetime'], jsonData['days'][i]['hours']
    for j in range(len(inday)):
      datetime = inday[j]['datetime']
      temp, rh = inday[j]['temp'], inday[j]['humidity']
      # print(date, datetime, ',temp:', temp, ',humidity:', rh)
      date_list.append(date)
      datetime_list.append(datetime)
      temp_list.append(temp)
      rh_list.append(rh)
  df = pd.DataFrame({'date':date_list, 'datetime':datetime_list, 'temp':temp_list, 'humidity':rh_list})
  return df
  
# api_key = "Q82HADKP8VA46L5QNL2LJLC4Y"
# lat, lon = 13.989478999999996, 100.616387 #z=17
# df = Visualcrossing_forecast(lat, lon, api_key)
# df
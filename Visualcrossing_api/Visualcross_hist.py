import csv
import json
import codecs
import urllib.request
import sys
import pandas as pd
from google.colab import files

########## historical data ##########
lat, lon = "13.989478999999996", "100.616387"
start_date, end_date = "2021-01-01", "2021-01-15"

# api_key = "Q82HADKP8VA46L5QNL2LJLC4Y" #Chula
# api_key = "2DSCEBCSZCZ87NGFDKK3Z84GB" #KU
api_key = "9ECDU5PSBATV5BF3VYZH2MRU4" #Thanksfordoo

def Visualcrossing_hist(lat, lon, start_date, end_date, api_key):
  url1 = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
  url2 = str(lat)+"%2C%20"+str(lon)+"/"+str(start_date)+"/"+str(end_date)
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
  dates, times = [], []
  temps, rhs = [], []
  for i in range(len(his_data)):
    date, data = his_data[i]['datetime'], his_data[i]['hours']
    for j in range(len(data)):
      datetime = data[j]['datetime']
      temp, rh = data[j]['temp'], data[j]['humidity']
      dates.append(date)
      times.append(datetime)
      temps.append(temp)
      rhs.append(rh)
  df = pd.DataFrame({'date':dates, 'time':times, 'temperature':temps, 'humidity':rhs})
  df.to_csv('Visualcrossing_'+str(start_date)+'_'+str(end_date)+'.csv') 
  # files.download('Visualcrossing_01_01_2021_15_01_2021.csv')
  return df

df = Visualcrossing_hist(lat, lon, start_date, end_date, api_key, url)
df
# IKHLON5, IMUEAN36, IPATHUMT2, VTBD
import time
import json
import datetime
import requests
import pandas as pd
from tqdm import tqdm
# from google.colab import files
# import tqdm

def wg_his_data(start, end, year, month, station_name, apiKey):
  days, obsTimeUtcs, obsTimeLocals, tempAvgs, humidityAvgs = [], [], [], [], []
  for i in range(start,end+1):
    days.append(datetime.date(year, month, i).strftime('%Y%m%d'))
  for day in tqdm(days):
    try:
      url = "https://api.weather.com/v2/pws/history/hourly?stationId="+str(station_name)+"&format=json&units=m&date="+str(day)+"&apiKey="+str(apiKey)
      payload, headers={}, {}
      response = requests.request("GET", url, headers=headers, data=payload)
      data = json.loads(response.text)
      stationID = data['observations'][0]['stationID']
      lat, lon = data['observations'][0]['lat'], data['observations'][0]['lon']
      for i in range(len(data['observations'])):
        obsTimeUtc, obsTimeLocal = data['observations'][i]['obsTimeUtc'], data['observations'][i]['obsTimeLocal']
        tempAvg, humidityAvg = data['observations'][i]['metric']['tempAvg'], data['observations'][i]['humidityAvg']
        obsTimeUtcs.append(obsTimeUtc); obsTimeLocals.append(obsTimeLocal);  
        tempAvgs.append(tempAvg); humidityAvgs.append(humidityAvg);    
    except:
      print('day: ', day)
      obsTimeUtcs.append(obsTimeUtc); obsTimeLocals.append(obsTimeLocal);
      tempAvgs.append(-99); humidityAvgs.append(-99);
  df = pd.DataFrame({'obsTimeUtc':obsTimeUtcs, 'obsTimeLocal':obsTimeLocals, 'tempAvg':tempAvgs, 'humidityAvg':humidityAvgs})
  return df

start, end, year, month = 1, 31, 2022, 3
days, obsTimeUtcs, obsTimeLocals, tempAvgs, humidityAvgs = [], [], [], [], []
station_name, apiKey = 'IPHOCH1', "92034bae5e864c0a834bae5e86fc0a18"
df = wg_his_data(start, end, year, month, station_name, apiKey)
df
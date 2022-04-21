import json
import requests
import pandas as pd

def current_tmd_data():
  sname_en_g, sname_th_g, Lat_g, Lon_g, temp_g, rh_g, datetime = [], [], [], [], [], [], []
  url = "http://data.tmd.go.th/api/WeatherToday/V1/?type=json"
  payload, headers={},  {'Authorization': 'Bearer 545d49361c74fe17c54806410ef1a738'}
  response = requests.request("GET", url, headers=headers, data=payload)
  r = json.loads(response.text); print(r['Header']);
  date = r['Header']['LastBuiltDate']
  for i in range(len(r['Stations'])):
    sname_en, sname_th = r['Stations'][i]['StationNameTh'], r['Stations'][i]['StationNameEng']
    Lat, Lon= round(float(r['Stations'][i]['Latitude']['Value']), 4), round(float(r['Stations'][i]['Longitude']['Value']),4)
    temp, rh = round(r['Stations'][i]['Observe']['Temperature']['Value'],2), round(r['Stations'][i]['Observe']['RelativeHumidity']['Value'],2)
    sname_en_g.append(sname_en); sname_th_g.append(sname_th);
    Lat_g.append(Lat); Lon_g.append(Lon);
    temp_g.append(temp); rh_g.append(rh); datetime.append(date);
    # print(str(i), sname_en, ":", sname_th, Lat, Lon, temp, rh)
  df = pd.DataFrame({'datetime':datetime, 'sname_en':sname_en_g, 'sname_th':sname_th_g, 'Lat':Lat_g, 'Lon':Lon_g, 'temp':temp_g, 'rh':rh_g})
  return df
df = current_tmd_data()
df
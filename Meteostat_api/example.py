#!pip install meteostat

import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from meteostat import Point, Daily, Hourly, Stations

# #### get hourly data from location Id : locationID, start, end
# start, end = datetime(2021, 1, 1), datetime(2021, 2, 28, 23, 59)
# data = Hourly('72219', start, end) #(location_ID, start, end)
# data = data.fetch()
# print(data)

# #### get daily data by lat lon 
# lat, long = 13.989478999999996, 100.616387
# start, end = datetime(2021, 1, 1), datetime(2021, 2, 28, 23, 59) 
# location = Point(lat, long, 70)
# data = Daily(location, start, end)
# data = data.fetch()
# print(data)
# data.plot(y=['tavg', 'tmin', 'tmax'])
# plt.show()

# #### Get closest weather station to your location [daily, hourly]
# lat, lon = 13.989478999999996, 100.616387
# start, end = datetime(2021, 1, 1), datetime(2021, 1, 15)
# stations = Stations()
# stations = stations.nearby(lat, lon)
# # stations = stations.inventory('daily', (start, end))
# stations = stations.inventory('hourly', (start, end))
# ## Fetch closest station (limit = 1)
# station = stations.fetch(1)
# station
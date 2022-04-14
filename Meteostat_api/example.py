#!pip install meteostat

import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from meteostat import Point, Daily, Hourly, Stations

#### get data from location Id : locationID, start, end
start, end = datetime(2021, 1, 1), datetime(2021, 2, 28, 23, 59)
data = Hourly('72219', start, end) #(location_ID, start, end)
data = data.fetch()
print(data)
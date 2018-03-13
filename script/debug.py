# debug if the latlng is correct
import pandas as pd
import numpy as np
import webroute as sh
import time
f = os.path.dirname(os.getcwd())+'/data/major_edges_lnglat.csv'
df = pd.read_csv(f)
df = df[(df['oneway']) & (df['length']>100)]
interval = 0.1
threshold = 60
r = {} # store the result
for i in df.index:
    time.sleep(interval)
    OBJECTID,f_lat,f_lng,t_lat,t_lng,road_length = df.loc[i,'OBJECTID'],df.loc[i,'from_lat_mars'],df.loc[i,'from_lng_mars'],df.loc[i,'to_lat_mars'],df.loc[i,'to_lng_mars'],df.loc[i,'length']
    r[OBJECTID]=sh.isShortest(f_lng,f_lat,t_lng,t_lat,road_length,threshold)

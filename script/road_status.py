import pandas as pd
import numpy as np
import webroute as sh
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
interval = 0.1
f1 = '/Users/left/WXRd/data/WX_ring/major_edges_lnglat.csv'
f2 = '/Users/left/WXRd/data/WX_ring/isShortest.csv'
df1 = pd.read_csv(f1,index_col='OBJECTID')
df2 = pd.read_csv(f2)

df2 = df2[df2['isShortest']]

f = open('road_status.txt','w+')
try:
    for i in df2.index:
        time.sleep(interval)
        t = time.ctime()
        obj_id = df2.loc[i,'OBJECTID']
        f_lat,f_lng,t_lat,t_lng = df1.loc[obj_id,'from_lat_mars'],df1.loc[obj_id,'from_lng_mars'],df1.loc[obj_id,'to_lat_mars'],df1.loc[obj_id,'to_lng_mars']
        distance,duation,status = sh.getStatus(f_lng,f_lat,t_lng,t_lat)
        f.write("%d,%f,%f,%s,%s\r" % (obj_id,distance,duation,status,time))
finally:
    f.close()

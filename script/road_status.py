import pandas as pd
import webroute as sh
import time
import os
interval = 0.05

hour = 600

f1 = os.path.dirname(os.getcwd())+'/data/major_edges_lnglat.csv'
f2 = os.path.dirname(os.getcwd())+'/data/isShortest.csv'
df1 = pd.read_csv(f1,index_col='OBJECTID')
df2 = pd.read_csv(f2)

df2 = df2[df2['isShortest']]

f = open(os.path.dirname(os.getcwd())+'road_status.txt','w+')
try:
    while(True):
        for i in df2.index:
            time.sleep(interval)
            t = time.ctime()
            obj_id = df2.loc[i,'OBJECTID']
            f_lat,f_lng,t_lat,t_lng = df1.loc[obj_id,'from_lat_mars'],df1.loc[obj_id,'from_lng_mars'],df1.loc[obj_id,'to_lat_mars'],df1.loc[obj_id,'to_lng_mars']
            distance,duation,status = sh.getStatus(f_lng,f_lat,t_lng,t_lat)
            f.write("%d,%f,%f,%s,%s\r\n" % (obj_id,distance,duation,status,t))
        time.sleep(hour)
finally:
    f.close()

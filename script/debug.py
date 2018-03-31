# debug if the latlng is correct
import pandas as pd
import numpy as np
import webroute as sh
import time
import os

f = os.path.dirname(os.getcwd())+'/data/137平方公里城区道路信息表火星坐标系.xlsx'
df = pd.read_excel(f)
interval = 0.01
threshold = 80
for i in df.index:
    time.sleep(interval)
    try:
    	OBJECTID,f_lat,f_lng,t_lat,t_lng,road_length = i,df.loc[i,'from_lat_mars'],df.loc[i,'from_lng_mars'],df.loc[i,'to_lat_mars'],df.loc[i,'to_lng_mars'],df.loc[i,'length']
    	df.loc[i,'isShortest']=sh.isShortest(f_lng,f_lat,t_lng,t_lat,road_length,threshold)
    except KeyError:
     	pass
df.to_excel('校核结果.excel')

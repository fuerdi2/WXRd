#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 12:35:14 2018

@author: left
"""
import pandas as pd
import numpy as np
f1 = '/Users/left/WXRd/data/WX_ring/major_edges_lnglat.csv'

f2 = '/Users/left/WXRd/data/WX_ring/isShortest.csv'

df1 = pd.read_csv(f1,index_col='OBJECTID')
df2 = pd.read_csv(f2)

markers = ''

for i in df2.index:
    objid = df2.loc[i,'OBJECTID']
    from_id = df1.loc[objid,'from_']
    from_lat = df1.loc[objid,'from_lat_mars']
    from_lng = df1.loc[objid,'from_lng_mars']
    to_id = df1.loc[objid,'to']
    to_lat,to_lng = df1.loc[objid,'to_lat_mars'],df1.loc[objid,'to_lat_mars']
    s = '{title:'+'\"'+str(from_id)+'\"'+',position:['+str(from_lng)+','+str(from_lat)+']},'+'{title:'+'\"'+str(to_id)+'\"'+',position:['+str(to_lng)+','+str(to_lat)+']},'
    markers = markers+s
with open('markers.txt','w') as f:
    f.write(markers)

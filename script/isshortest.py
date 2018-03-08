# isShortest

import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
class isShortest():
	url = 'http://restapi.amap.com/v3/direction/driving?'; # this is the webapi of Amap
	key = "79508e9bb55bd15284d6c5a097fe780c"; #this is yourKey
	stg = 2; #the shortest path driving strategy
	interval =0.1;
	def isShortest(f_lng,f_lat,t_lng,t_lat,threshold):
	    URL = url+"origin="+str(f_lng)+','+str(f_lat)+"&destination="+str(t_lng)+','+str(t_lat)+ \
	    "&strategy="+str(stg)+"&extensions=all&output=xml&key="+key;
	    try :
	        html = urlopen(URL);
	    except HTTPError as e:
	        print("URL error");
	    bsObj =  BeautifulSoup(html.read().decode("utf-8"));
	    routes = len(bsObj.steps);
	    distance = float(bsObj.route.path.distance.getText());
	    if(routes==0):
	        print("no steps");
	    return (routes==1 or abs(distance-threshold)<50);
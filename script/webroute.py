# isShortest
import time
import pandas as pd
from urllib.request import urlopen
from urllib import error
from bs4 import BeautifulSoup
url = 'http://restapi.amap.com/v3/direction/driving?'; # this is the webapi of Amap
key = "2609ba44c963af81305d291908f8f293"; #this is yourKey
key_qiye = 'a44238fae301d7143a9e40ae5f01d54d'
stg = 2; #the shortest path driving strategy
def isShortest(f_lng,f_lat,t_lng,t_lat,length,threshold):
	URL = url+"origin="+str(f_lng)+','+str(f_lat)+"&destination="+str(t_lng)+','+str(t_lat)+ \
	"&strategy="+str(stg)+"&extensions=all&output=xml&key="+key_qiye;
	try:
	    html = urlopen(URL);
	except error.URLError as e:
	    print(e.reason);
	bsObj =  BeautifulSoup(html.read().decode("utf-8"));
	try:
		routes = len(bsObj.steps);
	except TypeError:
		return (True)
	distance = float(bsObj.route.path.distance.getText());
	if(routes==0):
	    print("no steps");
	return 1 if(routes==1 or abs(distance-length)<threshold) else 0;
def getStatus(f_lng,f_lat,t_lng,t_lat):
	URL = url+"origin="+str(f_lng)+','+str(f_lat)+"&destination="+str(t_lng)+','+str(t_lat)+ \
	"&strategy="+str(stg)+"&extensions=all&output=xml&key="+key_qiye;
	try :
		html = urlopen(URL,timeout = 60);
	except error.URLError as e:
		print(e.reason);
	try:
		bsObj =  BeautifulSoup(html.read().decode("utf-8"));
		distance = float(bsObj.route.path.distance.getText())
		time = float(bsObj.route.path.duration.getText())
		status = bsObj.route.path.tmc.status.getText()
	except AttributeError:
		pass
	return distance,time,status
def getWeather():
	URL = 'http://restapi.amap.com/v3/weather/weatherInfo?key='+key+'&city=320200&output=xml'
	try :
		html = urlopen(URL,timeout = 60)
	except error.URLError as e:
		print(e.reason);
	try:
		bsObj =  BeautifulSoup(html.read().decode("utf-8"))
		tempe = float(bsObj.lives.temperature.getText())
		humid = float(bsObj.lives.humidity.getText())
		weather = str(bsObj.lives.weather.getText())
	except AttributeError:
		pass
	return tempe,humid,weather

import json
import requests 

f = open('subway.txt','w')
f.write("DATE" + '\t' + 'STATION' + '\t' + "PASSENGERS" + '\n')

url1 = 'http://openapi.seoul.go.kr:8088/6476564a4d6b79753730754253754b/json/CardSubwayStatsNew/1/500/20161008'
url2 = 'http://openapi.seoul.go.kr:8088/6476564a4d6b79753730754253754b/json/CardSubwayStatsNew/1/500/20161015'
url3 = 'http://openapi.seoul.go.kr:8088/6476564a4d6b79753730754253754b/json/CardSubwayStatsNew/1/500/20161022'
url4 = 'http://openapi.seoul.go.kr:8088/6476564a4d6b79753730754253754b/json/CardSubwayStatsNew/1/500/20161029'
url5 = 'http://openapi.seoul.go.kr:8088/6476564a4d6b79753730754253754b/json/CardSubwayStatsNew/1/500/20161105'
url6 = 'http://openapi.seoul.go.kr:8088/6476564a4d6b79753730754253754b/json/CardSubwayStatsNew/1/500/20161112'
url7 = 'http://openapi.seoul.go.kr:8088/6476564a4d6b79753730754253754b/json/CardSubwayStatsNew/1/500/20161119'
url8 = 'http://openapi.seoul.go.kr:8088/6476564a4d6b79753730754253754b/json/CardSubwayStatsNew/1/500/20161126'
url9 = 'http://openapi.seoul.go.kr:8088/6476564a4d6b79753730754253754b/json/CardSubwayStatsNew/1/500/20161203'

urllist = [url1,url2,url3,url4,url5,url6,url7,url8,url9]

for each_url in urllist: 
    resp = requests.get(url=each_url)
    data = json.loads(resp.text)

    city1 = data['CardSubwayStatsNew']['row'][1]
    city2 = data['CardSubwayStatsNew']['row'][10]
    palace = data['CardSubwayStatsNew']['row'][68]
    anguk = data['CardSubwayStatsNew']['row'][69]
    gwanghwamun = data['CardSubwayStatsNew']['row'][142]
    
    city1_num = city1['RIDE_PASGR_NUM']+city1['ALIGHT_PASGR_NUM']
    city2_num = city2['RIDE_PASGR_NUM']+city2['ALIGHT_PASGR_NUM']
    palace_num = palace['RIDE_PASGR_NUM']+palace['ALIGHT_PASGR_NUM']
    anguk_num = anguk['RIDE_PASGR_NUM']+anguk['ALIGHT_PASGR_NUM']
    gwanghwamun_num = gwanghwamun['RIDE_PASGR_NUM']+gwanghwamun['ALIGHT_PASGR_NUM']
    
    dt = each_url[-8:]
    
    f.write(dt + '\t' + "City Hall1" + "\t" + str(city1_num) + '\n')
    f.write(dt + '\t' + "City Hall2" + "\t" + str(city2_num) + '\n')
    f.write(dt + '\t' + "Palace" + "\t" + str(palace_num) + '\n')
    f.write(dt + '\t' + "Anguk" + "\t" + str(anguk_num) + '\n')
    f.write(dt + '\t' + "Gwanghwamun" + "\t" + str(gwanghwamun_num) + '\n')
    
    
f.close()
    



# 高德API + python 实现租房爬虫
# 1. 爬取58同城品牌公寓前20个页面,筛选条件为价格1500-2000
# 2. 爬取每个信息的 房源名称，地址，月租，房源url地址，经纬度，并写入相应的文件中
import csv
import re
from urllib import request
from bs4 import BeautifulSoup
pageNum=10

def getLonLat(string):
    pattern1=re.compile("_+json4fe\.lon = \'[0-9]+\.[0-9]+\';")
    lon=pattern1.findall(string)[0]
    pattern2=re.compile("[0-9]+\.[0-9]+")
    lon=pattern2.findall(lon)[0]

    pattern1=re.compile("_+json4fe\.lat = \'[0-9]+\.[0-9]+\';")
    lat=pattern2.findall(pattern1.findall(string)[0])[0]
    return [lon, lat]

#get info of each url
def getInfo(url):
    html=request.urlopen(url)
    bsObj=BeautifulSoup(html,'lxml')
    name=bsObj.title.text
    price=bsObj.find("span", class_="price").text
	# remove &nbsp
    price=re.sub(' *&nbsp','',price)
    script=bsObj.find('script').text
    lon_lat=getLonLat(script)
    writer.writerow((name,price,lon_lat[0],lon_lat[1],url))
		 
def craw(url):
    html=request.urlopen(url)
    bsObj=BeautifulSoup(html,'lxml')
    lists=bsObj.find_all('a',tongji_label="listclick")

    for list in lists:
        list=list.get('href')
        list="http://bj.58.com"+list
        print(list)
        try:
            getInfo(list)
        except Exception as e:
            print('Error', e)
            pass
    return

csvFile=open('data.csv','w')

writer = csv.writer(csvFile, delimiter=',')
writer.writerow(('名称','价格','经度','纬度','链接'))

page=1
while page <= pageNum:
    href="http://bj.58.com/pinpaigongyu/pn/"+str(page)+"/?minprice=1500_2000"
    craw(href)
    page=page+1
	
csvFile.close()

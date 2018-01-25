# 高德API + python 实现租房爬虫
# 1. 爬取58同城品牌公寓前20个页面,筛选条件为价格1500-2000
# 2. 爬取每个信息的 房源名称，地址，月租，房源url地址，经纬度，并写入相应的文件中
import csv
from urllib import request
from bs4 import BeautifulSoup
pageNum=1

def craw(url):
    html=request.urlopen(url)
    bsObj=BeautifulSoup(html,'lxml')
    lists=bsObj.find("ul",{"class":"list"}).children
    for list in lists:
	    print(list)
    return

csvFile=open('data.csv','w')

writer = csv.writer(csvFile)
writer.writerow(('名称','地址','价格','经度','纬度','链接'))
writer.writerow(('aaa','bbb','ccc','ddd','ddd','ddd'))

page=1
while page <= pageNum:
    href="http://bj.58.com/pinpaigongyu/pn/"+str(page)+"/?minprice=1500_2000"
    craw(href)
    page=page+1
	
csvFile.close()

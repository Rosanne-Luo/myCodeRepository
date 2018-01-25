# 高德API + python 实现租房爬虫
# 1. 爬取58同城品牌公寓前20个页面,筛选条件为价格1500-2000
# 2. 爬取每个信息的 房源名称，地址，月租，房源url地址，经纬度，并写入相应的文件中
import csv

def craw(url):
    print(url)
    return

csvFile=open('data.csv','w+')

writer = csv.writer(csvFile)
writer.writerow(('名称','地址','价格','经度','纬度','链接'))
writer.writerow(('aaa','bbb','ccc','ddd','ddd','ddd'))

for page in range(20):
    href="http://bj.58.com/pinpaigongyu/pn/"+str(page)+"/?minprice=1500_2000"
    craw(href)
	
csvFile.close()

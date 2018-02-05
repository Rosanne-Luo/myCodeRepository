from urllib import request
from bs4 import BeautifulSoup
import csv
#深圳，技术类岗位
url='https://hr.tencent.com/position.php?lid=2218&tid=87'
dataFile="tencentJob.csv"

def getDetailInfo(url):
	html=request.urlopen(url)
	bsObj=BeautifulSoup(html.read(),'lxml')
	table=bsObj.find('table',class_='tablelist textl')
	
	trList=table.find_all('tr')

	title=trList[0].find('td').string
	print(title)
	
	info2=trList[1].find_all('td')
	address=info2[0].text.split('：')[1]
	print(address)
	number=info2[2].text.split('：')[1]
	print(number)
	dutys=trList[2].find('ul').find_all(text=True)
	dutyStr=''
	for duty in dutys:
		dutyStr=dutyStr+duty
	print(dutyStr)
	demands=trList[3].find('ul').find_all(text=True)
	demandStr=''
	for demand in demands:
		demandStr=demandStr+demand
	print(demandStr)
	return [title, address, number, dutyStr, demandStr]

def getJob(url):
	html=request.urlopen(url)
	bsObj=BeautifulSoup(html.read(),'lxml')
	table=bsObj.find('table',class_='tablelist')
	trs=table.find_all('tr')
	trNum=len(trs)

#tr=trs[1]
	for tr in trs[1:trNum-1]:
		urlJob=tr.find('a')['href']
#print(type(urlJob))
		urlJob='https://hr.tencent.com/'+urlJob
		data=getDetailInfo(urlJob)
		csvWriter.writerow((data[0],data[1],data[2],data[3],data[4]))

#print(trs.prettify())
csvFile=open(dataFile,'w')
csvWriter=csv.writer(csvFile, delimiter=',')
csvWriter.writerow(('职位','工作地点','招聘人数','工作职责','工作要求'))
getJob(url)

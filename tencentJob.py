# 待添加功能：
# 1. 数据写入mysql
# 2. 实现多线程
# 3. 实现scapy架构

from urllib import request
from bs4 import BeautifulSoup
import csv
import re
import argparse

#深圳，技术类岗位
url='https://hr.tencent.com/position.php?lid=2218&tid=87&lid=2218&start='
dataFile="/Users/Rosanne/Desktop/tencentJob.csv"

#白名单记录我们需要查找的职位的关键词
#黑名单J留我们不需要查找的职位的关键词
whiteFilter='安全|研发|开发'
blackFilter='游戏|视觉|自然语言'

def getDetailInfo(url):
	html=request.urlopen(url)
	bsObj=BeautifulSoup(html.read(),'lxml')
	table=bsObj.find('table',class_='tablelist textl')
	
	trList=table.find_all('tr')

#获取职位名称,工作地点，招聘人数，工作职责，工作要求
	title=trList[0].find('td').string
	
	info2=trList[1].find_all('td')
	address=info2[0].text.split('：')[1]
	print(address)
	number=info2[2].text.split('：')[1]
	print(number)
	dutys=trList[2].find('ul').find_all(text=True)
	dutyStr=''
	for duty in dutys:
		dutyStr=dutyStr+'\n'+duty
	print(dutyStr)
	demands=trList[3].find('ul').find_all(text=True)
	demandStr=''
	for demand in demands:
		demandStr=demandStr+'\n'+demand
	print(demandStr)
	return [title, address, number, dutyStr, demandStr]

#对职位进行过滤，返回值为True表示我们需要进一步获取相关信息
def filterJob(job):
	w=re.search(whiteFilter,job)
	b=re.search(blackFilter,job)
	if (w and (not b)):
		return True
	else:
		return False

def getJob(url):
	html=request.urlopen(url)
	bsObj=BeautifulSoup(html.read(),'lxml')
	table=bsObj.find('table',class_='tablelist')
	trs=table.find_all('tr')
	trNum=len(trs)

	for tr in trs[1:trNum-1]:
		urlJob=tr.find('a')['href']
		job=tr.find('a').text
		if not filterJob(job):
				continue
		print("[*] get job: %s" % job)
		urlJob='https://hr.tencent.com/'+urlJob
		releaseData=tr.find_all('td')[4].string
		print(urlJob)
		try:
			data=getDetailInfo(urlJob)
			csvWriter.writerow((data[0],releaseData,data[1],data[2],data[3],data[4]))
		except Exception as e:
			pass
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--date", help="only get the info before the given date, the format is 2018-02-06")
	parser.add_argument("-u", "--update", help="just update the exsiting data file", action="store_true")
	args = parser.parse_args()
	if args.date:
        	date=args.date
	if args.update:
		mode="update"

	csvFile=open(dataFile,'w')
	csvWriter=csv.writer(csvFile, delimiter=',')
	csvWriter.writerow(('职位','发布时间','工作地点','招聘人数','工作职责','工作要求'))

	i=0
	while True:
		urlPage=url+str(i*10)+'#a'
		html=request.urlopen(urlPage)
		if not html:
			break
		print('[*] process page %d' % int(i+1))
		getJob(url)
		i=i+1

	csvFile.close()
	print('[*]finished')

if __name__ == '__main__':
	main()

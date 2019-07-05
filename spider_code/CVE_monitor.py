from bs4 import BeautifulSoup
from urllib import request
import csv

url = "https://cassandra.cerias.purdue.edu/CVE_changes/today.html"

def getCVEDetails(url):
	print(url)
	html=request.urlopen(url).read()
	bsObj=BeautifulSoup(html,'lxml')
#CVE-ID, Description, Date Entry Created
	table = bsObj.find(id='GeneratedTable').find('table')
	CVE_ID=table.find('h2').string
	print(CVE_ID)
	description=table.find_all('tr')[3].find('td').string
	data_created=table.find_all('tr')[10].find('td').string
	return [CVE_ID,description,data_created]

def getCVEList(url):
	html=request.urlopen(url).read()
	endStr=b"Graduations"
	CVEList_html=html[0:html.index(endStr)]
	bsObj=BeautifulSoup(CVEList_html,'lxml')
	lists=bsObj.find_all('a')
	for list in lists:
		print(list)
		data=getCVEDetails(list['href'])
		csvWriter.writerow((data[0],data[1],data[2]))


file=open('CVE_list.csv','w')
csvWriter=csv.writer(file,delimiter=',')
csvWriter.writerow(('CVE-ID','Description','date'))

getCVEList(url)

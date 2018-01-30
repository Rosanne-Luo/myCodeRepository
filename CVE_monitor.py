from bs4 import BeautifulSoup
from urllib import request
url = "https://cassandra.cerias.purdue.edu/CVE_changes/today.html"

def getCVEDetails(url):
		pass

def saveData(data):
		pass

def sendMail():
		pass

def getCVEList(url):
	html=request.urlopen(url).read()
	endStr=b"Graduations"
	CVEList_html=html[0:html.index(endStr)]
	bsObj=BeautifulSoup(CVEList_html,'lxml')
	lists=bsObj.find_all('a')
	for list in lists:
		data=getCVEDetails((list['href'])

getCVEList(url)

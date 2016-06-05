import urllib.request
import re
import sys
from bs4 import BeautifulSoup

class Parser:

	def __init__(self, addr='http://www.bankier.pl/gielda/notowania/akcje'):
		self.response = urllib.request.urlopen(addr)
		self.html = self.response.read()
		self.soup = BeautifulSoup(self.html, "html.parser")
		self.names=[]
		self.rates=[]
		self.parse()

	def parse(self):
		tagTr = self.soup.find_all("tr") #wyciagam wszystkie pola <tr>
		for it in tagTr:
			tagName=it.find_all("td",{"class" : "colWalor textNowrap"}) #wyciagam pola td o atrybucie class rownym colWalor textNowrap
			if len(tagName)>0:  
				tagRates=it.find_all("td")   #znajduje pola td
				rate=tagRates[1].text.replace(",",".")  #drugie pole td przechowuje wartość kursu, podmieniam , na .
				name=tagName[0].find("a").text  #w pierwszym polu td jest pola a, ktore przechowuje nazwe spolki
				self.rates.append(rate)
				self.names.append(name)



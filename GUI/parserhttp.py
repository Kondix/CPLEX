import urllib.request
import re
from bs4 import BeautifulSoup

class Parser:

	def __init__(self, addr='http://google.org/'):
		self.response = urllib.request.urlopen(addr)
		self.html = self.response.read()
		self.soup = BeautifulSoup(self.html, "html.parser")
		self.allBetsVector = []
		self.parse()

	def parse(self):
		self.allBetsNumbers = []
		self.allBetsDetailed = []
		
		self.allBets = self.soup.find_all(class_=re.compile('bet_item_info_id'))

		#wyciagamy wszystkie numery zakladow
		for c in self.allBets:
			self.allBetsNumbers.append(re.search('>(.+?)<', str(c)).group(1))
		#iteracja po col_bet oraz atrybucie z numerem zakladu
		for c in self.allBetsNumbers:
			self.allBetsDetailed.append(self.soup.find_all(attrs={'data-info':c}))
			#TODO: wyciaganie pustych betsów
		#dla kazdego wyciagamy zestaw bidów w kolejnosci
		for b in range(len(self.allBetsDetailed)):
			tempBetsVector = []
			for c in self.allBetsDetailed[b]:
				tempBetsVector.append(re.search('(.+?)</a>', str(c)).group(1))
			self.allBetsVector.append(tempBetsVector)
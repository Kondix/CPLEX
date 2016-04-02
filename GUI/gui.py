import tkinter as tk
from data import *
from parserhttp import *

class GUI(tk.Frame, Data):

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		self.m_data = Data()
		self.riskOrGainBool = 0
		self.betsVector = []

	def createWidgets(self):
		self.start = tk.Button(self)
		self.start["text"] = "Oblicz"
		self.start["command"] = self.downloadParseAndProcess
		self.start.pack(side="top")

		self.riskOrGain = tk.Checkbutton(self)
		self.riskOrGain["text"] = "Zaznacz aby wybrać obliczanie ryzyka.\nWyłączony oznacza kalkulacje zysku."
		self.riskOrGain["command"] = self.toggleRiskOrGain
		self.riskOrGain.pack()

		self.mainVar = tk.Entry(self)
		self.mainVar.insert(0, "Ryzyko/zysk")
		self.mainVar.pack(side = tk.LEFT)

		self.budget = tk.Entry(self)
		self.budget.insert(0, "Kwota")
		self.budget.pack(side = tk.LEFT)

		self.maxDay = tk.Entry(self)
		self.maxDay.insert(0, "Ilosc dni")
		self.maxDay.pack(side = tk.LEFT)

		self.minBet = tk.Entry(self)
		self.minBet.insert(0, "minBet")
		self.minBet.pack(side = tk.LEFT)

		self.maxBet = tk.Entry(self)
		self.maxBet.insert(0, "maxBet")
		self.maxBet.pack(side = tk.LEFT)

		self.scrollbar = tk.Scrollbar(root)
		self.scrollbar.pack(side = tk.LEFT, fill=tk.Y)
		self.betNamesList = tk.Listbox(root, yscrollcommand = self.scrollbar.set)
		self.betNamesList.pack(side = tk.LEFT, fill = tk.BOTH)
		self.scrollbar.config(command = self.betNamesList.yview)

	def downloadParseAndProcess(self):
		print("zaczynam liczenie")
		parser = Parser('https://www.efortuna.pl/pl/strona_glowna/serwis_sportowy/nba/index.html')
		self.betsVector = parser.allBetsVector
		print(self.betsVector)
		self.__accumulateData()
		self.__fillBetNamesList()
		#TODO: algorytm liczenia

	def __accumulateData(self):
		print("zbieram dane")
		self.m_data = Data(self.riskOrGainBool, self.mainVar.get(), self.budget.get(), self.maxDay.get(), self.minBet.get(), self.maxBet.get())

	def __fillBetNamesList(self):
		self.betNamesList.delete(0, tk.END)
		print("uzupelniam liste")
		for idx in range(len(self.betsVector)):
   			self.betNamesList.insert(tk.END, str(self.betsVector[idx][0]))


	def toggleRiskOrGain(self):
		print("przelaczam obliczanie ryzyka i zysku")
		self.riskOrGainBool = (self.riskOrGainBool+1)%2

root = tk.Tk()
app = GUI(master=root)
app.mainloop()

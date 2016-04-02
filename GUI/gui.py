import tkinter as tk
from data import *
from parserhttp import *
from datgenerator import *

class GUI(tk.Frame, Data):

	def __init__(self, master=None):
		self.betButtons = []

		tk.Frame.__init__(self, master)
		self.pack()

		self.buttonFrame = tk.Frame(self)
		self.buttonFrame.pack()

		self.dataFrame = tk.Frame(self)
		self.dataFrame.pack(pady = 5)

		self.presentationFrame = tk.Frame(self)
		self.presentationFrame.pack(side = tk.LEFT)

		self.betsFrame = tk.Frame(self)
		self.betsFrame.pack(side = tk.LEFT, fill = tk.X, padx = 5)		

		self.createWidgets()
		self.m_data = Data()
		self.riskOrGainBool = 0
		self.betsVector = []

	def createWidgets(self):
		self.__initButtonFrame()
		self.__initDataFrame()
		self.__initPresentationFrame()
		self.__initBetsFrame()

	def __initButtonFrame(self):
		self.start = tk.Button(self.buttonFrame)
		self.start["text"] = "Pobierz"
		self.start["command"] = self.downloadParse
		self.start.pack(side=tk.LEFT, fill = tk.BOTH)

		self.start = tk.Button(self.buttonFrame)
		self.start["text"] = "Oblicz"
		self.start["command"] = self.startProcessing
		self.start.pack(side=tk.LEFT, fill = tk.BOTH)

	def __initDataFrame(self):
		self.riskOrGain = tk.Checkbutton(self.dataFrame)
		self.riskOrGain["text"] = "Zaznacz aby wybrać obliczanie ryzyka.\nWyłączony oznacza kalkulacje zysku."
		self.riskOrGain["command"] = self.toggleRiskOrGain
		self.riskOrGain.pack(side = tk.TOP)

		self.mainVar = tk.Entry(self.dataFrame)
		self.mainVar.insert(0, "Ryzyko/zysk")
		self.mainVar.pack(side = tk.BOTTOM)

		self.budget = tk.Entry(self.dataFrame)
		self.budget.insert(0, "Kwota")
		self.budget.pack(side = tk.BOTTOM)

		self.maxDay = tk.Entry(self.dataFrame)
		self.maxDay.insert(0, "Ilosc dni")
		self.maxDay.pack(side = tk.BOTTOM)

		self.minBet = tk.Entry(self.dataFrame)
		self.minBet.insert(0, "minBet")
		self.minBet.pack(side = tk.BOTTOM)

		self.maxBet = tk.Entry(self.dataFrame)
		self.maxBet.insert(0, "maxBet")
		self.maxBet.pack(side = tk.BOTTOM)

	def __initPresentationFrame(self):
		self.scrollbar = tk.Scrollbar(self.presentationFrame)
		self.scrollbar.pack(side = tk.LEFT, fill=tk.Y)
		self.betNamesList = tk.Listbox(self.presentationFrame, yscrollcommand = self.scrollbar.set)
		self.betNamesList.bind('<<ListboxSelect>>', self.onBetSelect)
		self.betNamesList.pack(side = tk.LEFT, fill = tk.Y)
		self.scrollbar.config(command = self.betNamesList.yview),

	def __initBetsFrame(self):

		self.bet1 = tk.Button(self.betsFrame)
		self.bet1["text"] = "bet1"
		self.bet1["command"] = lambda: self.__toggleBetColor(0)
		self.bet1.pack(side=tk.LEFT, fill = tk.BOTH)
		self.betButtons.append(self.bet1)

		self.bet2 = tk.Button(self.betsFrame)
		self.bet2["text"] = "bet2"
		self.bet2["command"] = lambda: self.__toggleBetColor(1)
		self.bet2.pack(side=tk.LEFT, fill = tk.BOTH)
		self.betButtons.append(self.bet2)

		self.bet3 = tk.Button(self.betsFrame)
		self.bet3["text"] = "bet3"
		self.bet3["command"] = lambda: self.__toggleBetColor(2)
		self.bet3.pack(side=tk.LEFT, fill = tk.BOTH)
		self.betButtons.append(self.bet3)

		self.bet4 = tk.Button(self.betsFrame)
		self.bet4["text"] = "bet4"
		self.bet4["command"] = lambda: self.__toggleBetColor(3)
		self.bet4.pack(side=tk.LEFT, fill = tk.BOTH)
		self.betButtons.append(self.bet4)

		self.bet5 = tk.Button(self.betsFrame)
		self.bet5["text"] = "bet5"
		self.bet5["command"] = lambda: self.__toggleBetColor(4)
		self.bet5.pack(side=tk.LEFT, fill = tk.BOTH)
		self.betButtons.append(self.bet5)

	def onBetSelect(self, evt):
		w = evt.widget
		index = int(w.curselection()[0])
		#value = w.get(index) //moze byc przydatne
		for idx in range(5):
			self.betButtons[idx]['text'] = self.betsVector[index][idx+2]

	def downloadParse(self):
		print("zaczynam pobieranie")
		parser = Parser('https://www.efortuna.pl/pl/strona_glowna/serwis_sportowy/nba/index.html')
		self.betsVector = parser.allBetsVector
		print(self.betsVector)
		self.__fillBetNamesList()

	def startProcessing(self):
		print("zaczynam liczenie")
		self.__accumulateData()
		datGen = DatGenerator(self.m_data)
		datGen.generateDatFile()
		#TODO: algorytm liczenia

	def __accumulateData(self):
		print("zbieram dane")
		self.m_data = Data(self.riskOrGainBool, self.mainVar.get(), self.budget.get(), self.maxDay.get(), self.minBet.get(), self.maxBet.get())

	def __fillBetNamesList(self):
		self.betNamesList.delete(0, tk.END)
		print("uzupelniam liste")
		for idx in range(len(self.betsVector)):
   			self.betNamesList.insert(tk.END, str(self.betsVector[idx][1]))

	def toggleRiskOrGain(self):
		print("przelaczam obliczanie ryzyka i zysku")
		self.riskOrGainBool = (self.riskOrGainBool+1)%2

	def __toggleBetColor(self, idx):
		colors = ['SystemButtonFace', 'green']
		self.betButtons[idx].configure(bg = colors[(colors.index(self.betButtons[idx]['bg'])+1)%2])


root = tk.Tk()
app = GUI(master=root)
app.mainloop()
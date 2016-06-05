import tkinter as tk
from parserhttp import *
from data import *
import cplexalgorithm as cpx

class GUI(tk.Frame):

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.data = Data()
		
		self.buttonFrame = tk.Frame(self)
		self.buttonFrame.pack()
		
		
		self.dataFrame = tk.Frame(self)
		self.dataFrame.pack(pady = 5)
		
		
		self.list1Frame = tk.Frame(self)
		self.list1Frame.pack(side = tk.LEFT)
		
		self.list2Frame = tk.Frame(self)
		self.list2Frame.pack(side = tk.RIGHT)
		
		self.createWidgets()
		
		self.usedIndex = []


	def createWidgets(self):
		self.__initButtonFrame()
		self.__initDataFrame()
		self._initListBox1()
		self._initListBox2()

	def _initListBox1(self):
		self.scrollbar = tk.Scrollbar(self.list1Frame)
		self.scrollbar.pack(side = tk.LEFT, fill=tk.Y)
		self.companiesList = tk.Listbox(self.list1Frame, yscrollcommand = self.scrollbar.set)
		self.companiesList.bind('<<ListboxSelect>>', self.onCompanySelect)
		self.companiesList.pack(side = tk.LEFT, fill = tk.Y)
		self.scrollbar.config(command = self.companiesList.yview),
		
	def onCompanySelect(self, evt):
		w = evt.widget
		index = int(w.curselection()[0])
		self.usedIndex.append(index)
		self.moveToList2Box(self.companiesList.get(index))

	def onChosenCompanySelect(self, evt):
		w = evt.widget
		index = int(w.curselection()[0])
		#value = w.get(index) //moze byc przydatn
		self.chosenCompaniesList.delete(index)
                

	def _initListBox2(self):
		self.scrollbar = tk.Scrollbar(self.list2Frame)
		self.scrollbar.pack(side = tk.RIGHT, fill=tk.Y)
		self.chosenCompaniesList = tk.Listbox(self.list2Frame, yscrollcommand = self.scrollbar.set)
		self.chosenCompaniesList.bind('<<ListboxSelect>>', self.onChosenCompanySelect)
		self.chosenCompaniesList.pack(side = tk.LEFT, fill = tk.Y)
		self.scrollbar.config(command = self.chosenCompaniesList.yview),
		
	def moveToList2Box(self, company):
		self.chosenCompaniesList.insert(tk.END, str(company))
		
	def __initButtonFrame(self):
		self.start = tk.Button(self.buttonFrame)
		self.start["text"] = "Pobierz"
		self.start["command"] = self.downloadParse
		self.start.pack(side=tk.LEFT, fill = tk.BOTH)

		self.start = tk.Button(self.buttonFrame)
		self.start["text"] = "Zapisz kursy"
		self.start["command"] = self.saveToFile
		self.start.pack(side=tk.LEFT, fill = tk.BOTH)
		
		self.start = tk.Button(self.buttonFrame)
		self.start["text"] = "Oblicz"
		self.start["command"] = self.startProcessing
		self.start.pack(side=tk.LEFT, fill = tk.BOTH)
		
	def __initDataFrame(self):
		self.budget = tk.Entry(self.dataFrame)
		self.budget.insert(0, "Srodki pieniezne [PLN]")
		self.budget.pack(side = tk.BOTTOM)
		
		self.gain = tk.Entry(self.dataFrame)
		self.gain.insert(0, "Pozadany zysk [%]")
		self.gain.pack(side = tk.BOTTOM)

	def downloadParse(self):
		print("zaczynam pobieranie")
		parser = Parser('http://www.bankier.pl/gielda/notowania/akcje')
		self.namesList = parser.names
		self.ratesList = parser.rates
		print(self.namesList)
		print(self.ratesList)
		self.__fillList1()
	def __fillList1(self):
		self.companiesList.delete(0, tk.END)
		print("uzupelniam liste")
		for idx in range(len(self.namesList)):
			self.companiesList.insert(tk.END, str(self.namesList[idx]) + '---' + str(self.ratesList[idx]))
			
	def setData(self):
		rdyToCpyRates= []
		rdyToCpyNames= []
		for i in range(len(self.usedIndex)):
			rdyToCpyRates.append(self.ratesList[int(self.usedIndex[i])])
			rdyToCpyNames.append(self.namesList[int(self.usedIndex[i])])
		self.data = Data(self.budget.get(), self.gain.get(), rdyToCpyRates, rdyToCpyNames)
		
	def startProcessing(self):
		self.setData()
		algo = cpx.cplexModel(self.data)
		algo.getValue()
		
	def saveToFile(self):
		self.setData()
		self.data.generateDatFile()

root = tk.Tk()
app = GUI(master=root)
app.mainloop()

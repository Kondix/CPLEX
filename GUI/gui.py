import tkinter as tk
from data import *

class GUI(tk.Frame):

	m_data = Data()

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

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
		self.mainVar.pack()

		self.budget = tk.Entry(self)
		self.budget.insert(0, "Kwota")
		self.budget.pack()

		self.maxDay = tk.Entry(self)
		self.maxDay.insert(0, "Ilosc dni")
		self.maxDay.pack()

		self.minBet = tk.Entry(self)
		self.minBet.insert(0, "minBet")
		self.minBet.pack()

		self.maxBet = tk.Entry(self)
		self.maxBet.insert(0, "maxBet")
		self.maxBet.pack()

		self.quit = tk.Button(self, text="Wyłącz", fg="red",
                                            command=root.destroy)
		self.quit.pack(side="bottom")

	def downloadParseAndProcess(self):
		print("zaczynam liczenie")
		self.__accumulateData()
		#TODO: algorytm liczenia

	def __accumulateData(self):
		print("zbieram dane")
		m_data.riskOrBudg = 0
		m_data.mainVar = self.mainVar.get()
		m_data.budget = self.budget.get()
		m_data.maxDay = self.maxDay.get()
		m_data.minBet = self.minBet.get()
		m_data.maxBet = self.maxBet.get()

	def toggleRiskOrGain(self):
		print("przelaczam obliczanie ryzyka i zysku")
		#TODO: ustawienie flagi do kalkulacji w parserze

root = tk.Tk()
app = GUI(master=root)
app.mainloop()

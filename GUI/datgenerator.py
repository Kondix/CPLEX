import datetime as dt
from datetime import date
from time import strftime

class DatGenerator:

	def __init__(self, data): ##potrzebuje przekazywac dane: tablica kursów < nowa klasa i nowy argument
		print("rozpoczynam.")
		self.data=data

	def generateDatFile(self): 
		print('generuje plik .dat ...')
		f = open('project.dat', 'w')
		##f.write('/*********************************************\n * OPL 12.6.3.0 Data\n * Creation Date: ')
		###f.write(strftime('%Y-%m-%d at %H:%M:%S\n'))
		##f.write(' * Automatically generated file.\n*********************************************/\n\n')
		##f.write('nEvents=' + ?? + '; //ID, rate1, rate0, rate2, rate10, rate 02\n') ##<<liczba kolumn w tablicy kursów - 1 (nazwa druzyn ktore graja)
		##f.write('nBets='+ ?? +';\n')  ##<<liczba meczów
		#f.write('riskGain=' + str(self.data.riskOrGain) +'; //risk[0] or Gain[1]\n')
		f.write(self.data.budget+',')
		f.write(str(self.data.riskOrGain))
		f.close()
		print('wygenerowano: ' + strftime('%Y-%m-%d at %H:%M:%S\n'))
		return f.name
		
		
        
		#f.write('budget=' + self.data.budget +'; //Budget Value\n')
		#f.write('mainVar' + self.data.mainVar +'; //Risk||Gain Value\n')
		##f.write('ratesTable=[ ')
		##TODO petla wpisujaca pola do tablicy.
		##f.write('];\n')
		

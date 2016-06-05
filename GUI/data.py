import os.path

class Data:
	
	datFileName='Proje2kt.dat'
	
	def __init__(self, budg = 0, gain = 0 , k = [0], n =[0]):
		self.minGain = gain
		self.budget = budg
		self.rates = k
		self.names = n
		print('Przekazuje dane'+ 'budżet ' + str(self.budget)+ 'oczekiwany zysk ' + str(self.minGain)+ 'wybrane spółki i kursy ' + str(self.names) + '/' + str(self.rates))
		
	def generateDatFile(self):
		if os.path.isfile(self.datFileName):
			datFile=open(self.datFileName,'r')
			lines=datFile.readlines()
			datFile.close()
			datFile=open(self.datFileName,'w')
			datFile.truncate(0)
			datFile.write("budget="+str(self.budget)+";\n")
			datFile.write("minGain="+str(self.minGain)+";\n")
			datFile.write("nCurrencies="+str(len(self.names))+";\n")
			datFile.write("nSamples="+str(len(lines)-6)+";\n")
			datFile.write("names=[")
			for name in self.names[:-1]:
				datFile.write("\""+name+"\",")
			datFile.write("\""+name+"\"];\n")

			datFile.write("quotes=[\n")
			for line in lines[6:(len(lines)-1)]:
				datFile.write(line)
			datFile.write("[")
			for rate in self.rates[:-1]:
				datFile.write(rate+",")
			datFile.write(rate+"]\n];")
		
		else:
			datFile=open(self.datFileName,'a')
			datFile.write("budget="+str(self.budget)+";\n")
			datFile.write("minGain="+str(self.minGain)+";\n")
			datFile.write("nCurrencies="+str(len(self.names))+";\n")
			datFile.write("nSamples=1;\n")
			datFile.write("names=[")
			for name in self.names[:-1]:
				datFile.write("\""+name+"\",")
			datFile.write("\""+name+"\"];\n")

			datFile.write("quotes=[\n[")
			for rate in self.rates[:-1]:
				datFile.write(rate+",")
			datFile.write(rate+"]\n];")
		datFile.close()

	# def calculatePValue(self, kVector, mrg):
				# self.p[:] = []
				# for n in range(len(kVector)):
					# self.p.append(1/(kVector[n]*(1/(1-mrg))))
	# def calculatePKValue(self, kVector, pVector):
				# self.pk[:] = []
				# for n in range(len(kVector)):
					# self.pk.append(kVector[n]*pVector[n])

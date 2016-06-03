
class Data:
	p= []#P - wektor prawdopodobieństw:
	k= [1.8, 2.7, 3.6]#k - wektor kursów
	pk= []
	mrg = 0.2
	
	def __init__(self, rob = 0, mVar = 0, budg = 0 , maxD = 0, minB = 0, maxB = 0):
		self.riskOrGain = rob
		self.mainVar = mVar
		self.budget = budg
		self.maxDay = maxD
		self.minBet = minB
		self.maxBet = maxB
		self.calculatePValue(self.k, self.mrg)
		self.calculatePKValue(self.k, self.p)
		print(self.p)

	def calculatePValue(self, kVector, mrg):
				self.p[:] = []
				for n in range(len(kVector)):
					self.p.append(1/(kVector[n]*(1/(1-mrg))))
	def calculatePKValue(self, kVector, pVector):
				self.pk[:] = []
				for n in range(len(kVector)):
					self.pk.append(kVector[n]*pVector[n])

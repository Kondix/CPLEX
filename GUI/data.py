
class Data:
	p= []
	#P - wektor prawdopodobieństw:
	def __init__(self, rob = 0, mVar = 0, budg = 0 , maxD = 0, minB = 0, maxB = 0):
		self.riskOrGain = rob
		self.mainVar = mVar
		self.budget = budg
		self.maxDay = maxD
		self.minBet = minB
		self.maxBet = maxB

	def calculatePValue(self, kVector):
		for n in range(len(kVector)):
			self.p.append(1/((kVector[n]-1)*5/4+1))



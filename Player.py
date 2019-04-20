class player(object):
	def __init__(self, nname, seatNum):
		self.name = nname
		self.hand = None
		self.hasLead = False
		self.points = 0
		self.numTricks = 0
		self.seat = seatNum
		
	def setName(self, nname):
		self.name = nname
		
	def getName(self):
		return self.name
		
	def setHand(self, newHand):
		self.hand = newHand
		
	def getHand(self):
		return self.hand
		
	def getSeat(self):
		return self.seat
		
	def lead(self):
		self.hasLead = True
		
	def notLead(self):
		self.hasLead = False
		
	def takeTurn(self):
		print("************************" + self.name + "'s turn" + "************************")
		for c in self.hand:
			print( str(self.hand.index(c)) + ". " + c.toString())
		ind = input("Please pick a card to play: ")
		return self.hand.pop(int(ind))
	
	def regWin(self, p):
		self.points = self.points + p
	
	def regTrick(self):
		self.numTricks = self.numTricks + 1
		
	def getPoints(self):
		return self.points
		
	def getTricks(self):
		return self.numTricks
	
	def regV(self):
		print("We Did It!")
class card(object):
	def __init__(self, newRank, newSuit):
		self.rank = newRank
		self.suit = newSuit
		
	def setRank(self, newRank):
		self.rank = newRank
		
	def setSuit(self, newSuit):
		self.suit = newSuit
		
	def getRank(self):
		return self.rank
		
	def getSuit(self):
		return self.suit
		
	def compareSuit(self, nsuit):
		return self.getSuit() == nsuit
	
	# NOT WORKING
	def compareRank(self, nrank):
		if(self.getRank() == "2"):
			if(nrank.getRank() != "2"):
				return -1
		elif(self.getRank() == "3"):
			if(nrank.getRank() != "2" and nrank.getRank() != "3"):
				return -1
		elif(self.getRank() == "4"):
			if(nrank.getRank() != "2" and nrank.getRank() != "3" and nrank.getRank() != "4"):
				return -1
		elif(self.getRank() == "5"):
			if(nrank.getRank() != "2" and nrank.getRank() != "3" and nrank.getRank() != "4" and nrank.getRank() != "5"):
				return -1
		elif(self.getRank() == "6"):
			if(nrank.getRank() != "2" and nrank.getRank() != "3" and nrank.getRank() != "4" and nrank.getRank() != "5" and nrank.getRank() != "6"):
				return -1
		elif(self.getRank() == "7"):
			if(nrank.getRank() != "2" and nrank.getRank() != "3" and nrank.getRank() != "4" and nrank.getRank() != "5" and nrank.getRank() != "6" and nrank.getRank() != "7"):
				return -1
		elif(self.getRank() == "8"):
			if(nrank.getRank() != "2" and nrank.getRank() != "3" and nrank.getRank() != "4" and nrank.getRank() != "5" and nrank.getRank() != "6" and nrank.getRank() != "7" and nrank.getRank() != "8"):
				return -1
		elif(self.getRank() == "9"):
			if(nrank.getRank() != "2" and nrank.getRank() != "3" and nrank.getRank() != "4" and nrank.getRank() != "5" and nrank.getRank() != "6" and nrank.getRank() != "7" and nrank.getRank() != "8" and nrank.getRank() != "9"):
				return -1
		elif(self.getRank() == "10"):
			if(nrank.getRank() != "2" and nrank.getRank() != "3" and nrank.getRank() != "4" and nrank.getRank() != "5" and nrank.getRank() != "6" and nrank.getRank() != "7" and nrank.getRank() != "8" and nrank.getRank() != "9" and nrank.getRank() != "10"):
				return -1
		elif(self.getRank() == "Jack"):
			if(nrank.getRank() != "2" and nrank.getRank() != "3" and nrank.getRank() != "4" and nrank.getRank() != "5" and nrank.getRank() != "6" and nrank.getRank() != "7" and nrank.getRank() != "8" and nrank.getRank() != "9" and nrank.getRank() != "10" and nrank.getRank() != "Jack"):
				return -1
		elif(self.getRank() == "Queen"):
			if(nrank.getRank() != "2" and nrank.getRank() != "3" and nrank.getRank() != "4" and nrank.getRank() != "5" and nrank.getRank() != "6" and nrank.getRank() != "7" and nrank.getRank() != "8" and nrank.getRank() != "9" and nrank.getRank() != "10" and nrank.getRank() != "Jack" and nrank.getRank() != "Queen"):
				return -1
		elif(self.getRank() == "King"):
			if(nrank.getRank() != "2" and nrank.getRank() != "3" and nrank.getRank() != "4" and nrank.getRank() != "5" and nrank.getRank() != "6" and nrank.getRank() != "7" and nrank.getRank() != "8" and nrank.getRank() != "9" and nrank.getRank() != "10" and nrank.getRank() != "Jack" and nrank.getRank() != "Queen" and nrank.getRank() != "King"):
				return -1
		
		return 1
		
	def toString(self):
		return self.rank + " of " + self.suit
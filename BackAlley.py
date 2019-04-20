from Card import card
from Deck import deck
from Player import player
# from AI import ai
		
class game(object):
	def __init__(self):
		self.trump = None
		self.handSize = None
		self.maxHandSize = 10
		self.players = []
		self.deck = deck()
		self.lead = None
		self.cardStack = []
		
	def setTrump(self, tcard):
		self.trump = tcard
	
	def getTrump(self):
		return self.trump
	
	def addPlayer(self, p):
		self.players.append(p)
		
	def mainLoop(self):
		# first half of the game
		for i in range(1, self.maxHandSize + 1):
			
			self.handSize = i
			
			for p in self.players:
				p.setHand(self.deck.dealHand(self.handSize))
			self.setTrump(self.deck.dealHand(1).pop(0))
			
			for j in range(0, self.handSize):
				self.lead = self.players.pop(0)
				winningPlayer = self.lead
				cardLead = self.lead.takeTurn()
				
				for p in self.players:
					playedCard = p.takeTurn()
					if (playedCard.compareSuit(cardLead) and playedCard.compareRank(cardLead) > 0):
						cardLead = playedCard
						winningPlayer = p
				print(winningPlayer.getName())
				winningPlayer.regTrick()
				self.players.append(self.lead)
				self.lead = 
				
			for p in self.players:
				p.regWin(p.getTricks())
			
			self.deck.resetDeck()
		
		# second half of the game
		for i in range(1, self.maxHandSize + 1):
		
			self.handSize = self.maxHandSize - i
		
			for p in self.players:
				p.setHand(self.deck.dealHand(self.handSize))
			self.setTrump(self.deck.dealHand(1).pop(0))
			
			for j in range(0, self.handSize):
				self.lead = self.players.pop(0)
				winningPlayer = self.lead
				cardLead = self.lead.takeTurn()
				
				for p in self.players:
					playedCard = p.takeTurn()
					if (playedCard.compareSuit(cardLead) and playedCard.compareRank(cardLead) > 0):
						cardLead = playedCard
						winningPlayer = p
				print(winningPlayer.getName())
				winningPlayer.regTrick()
				
			for p in self.players:
				p.regWin(p.getTricks())
			
			self.players.append(self.lead)
			self.deck.resetDeck()
		
		winner = self.players.pop(0)
		for p in self.players:
			if(winner.getPoints() < p.getPoints()):
				winner = p
				
		print("WINNER: " + winner.getName())
		winner.regV()
			
##################################################MAIN##################################################

g = game()
g.addPlayer(player("sally", 0))
# g.addPlayer(player("jimmy", 1))
# g.addPlayer(player("katy", 2))
# g.addPlayer(player("Johny", 3))
# g.addPlayer(player("Susie", 4))
g.mainLoop()
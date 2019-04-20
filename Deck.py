import copy, random
from Card import card

class deck(object):
	def __init__(self):
		self.SUITS = ["Clubs", "Hearts", "Diamonds", "Spades"]
		self.RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		
		self.deckStart = []
		for suit in self.SUITS:
			for rank in self.RANKS:
				self.deckStart.append(card(rank, suit))
		
		self.playDeck = copy.deepcopy(self.deckStart)
		random.shuffle(self.playDeck)
		
	def shuffleDeck(self):
		random.shuffle(self.playDeck)
		
	def resetDeck(self):
		self.playDeck = copy.deepcopy(self.deckStart)
		random.shuffle(self.playDeck)
		
	def dealHand(self, size):
		hand = []
		for i in range(0, size):
			hand.append(self.playDeck.pop(0))
		return hand
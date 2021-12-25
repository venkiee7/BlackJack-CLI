class deck:
	def __init__(self,Hearts = {},Clubs = {},Spade = {} ,Diamond = {},card_deck = {}):
		self.Hearts = Hearts
		
		for i in range(2,11):
			self.Hearts.update({f'{i}\u2665':i})
		self.Hearts.update({'A\u2665':11,'J\u2665':10,'Q\u2665':10,'K\u2665':10})
		self.Clubs= Clubs
		for i in range(2,11):
			self.Clubs.update({f'{i}\u2663':i})
		self.Clubs.update({'A\u2663':11,'J\u2663':10,'Q\u2663':10,'K\u2663':10})
		self.Spade = Spade
		for i in range(2,11):
			self.Spade.update({f'{i}\u2660':i})
		self.Spade.update({'A\u2663':11,'J\u2660':10,'Q\u2660':10,'K\u2660':10})
		self.Diamond = Diamond
		for i in range(2,11):
			self.Diamond.update({f'{i}\u2666':i})
		self.Diamond.update({'A\u2663':11,'J\u2666':10,'Q\u2666':10,'K\u2666':10})
		self.card_deck = card_deck
		self.card_deck.update(self.Hearts)
		self.card_deck.update(self.Clubs)
		self.card_deck.update(self.Spade)
		self.card_deck.update(self.Diamond)
cards = deck()

		
		
		 
 


import time
import random
from deck import cards 
class rangili:
	def __init__(self,dealer_points = 0):
		self.dealer_points = dealer_points
		pass
	def DF2C(self):
		self.dcount = 0
		self.idcards = {}
		self.dface =''
		self.dvalue =0
		while self.dcount < 2: 
			
			self.dface , self.dvalue= random.choice(list(cards.card_deck.items()))
			self.dealer_points += self.dvalue 
			self.idcards.update({self.dface:self.dvalue})
			
			self.dcount += 1
		temp = list(self.idcards.keys())
		temp.pop(1)
		temp.append('Hidden Card')
		print(temp)
		
		
			
	def hit(self):
		while self.dealer_points <= 17:
				
				self.dface , self.dvalue= random.choice(list(cards.card_deck.items()))
				if self.dface == 'A\u2665' or self.dface == 'A\u2666' or self.dface == 'A\u2663' or self.dface == 'A\u2660' :
					if 21 <= (self.dealer_points + 11):
						self.dvalue = 11
					else:
						self.dvalue = 1
				self.dealer_points += self.dvalue 
				self.idcards.update({self.dface:self.dvalue})
				print(f'{list(self.idcards.keys())}')
				
				
			
			

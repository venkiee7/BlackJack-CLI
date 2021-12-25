import random
from deck import cards
class player:
	
	def __init__(self,player_points = 0,balance = 1000,bet = 0,player_name = '',records = {}):
		self.records = records
		self.player_name = player_name
		self.player_points = player_points 
		self.balance = balance
		self.bet = bet
		pass	
	def F2C(self):
		self.count = 0
		self.ipcards = {}
		self.face =''
		self.value =0
		while self.count < 2: 
			
			self.face , self.value= random.choice(list(cards.card_deck.items()))
			self.player_points += self.value 
			self.ipcards.update({self.face:self.value})
			self.count += 1
		print(f'{list(self.ipcards.keys())}')
		


	def hit_or_stay(self):
		while self.player_points<=21:
			choice = input('Do you want to hit:(Y or N)\n')
			if choice == 'y' or choice == 'Y': 
				
					self.face , self.value= random.choice(list(cards.card_deck.items()))
					if self.face == 'A\u2665' or self.face == 'A\u2666' or self.face == 'A\u2663' or self.face == 'A\u2660' :
						if 21 >= (self.player_points + 11):
							self.value = 11
						else:
							self.value = 1
					self.player_points += self.value 
					if self.face in self.ipcards:
						continue
					self.ipcards.update({self.face:self.value})
					print(f'{list(self.ipcards.keys())}')
					
					
					
				
			elif choice == 'N' or choice == 'n':
				print('You choose to stay')
				break
			else:
				print('Please choose a valid option')
				continue
		








		




import players
import dealers
import random


from deck import cards



p1 = players.player()
dealer = dealers.rangili()



def display():
	print('This is a BlackJack Game.\nInitialy you will be given $1000 to Gamble with.\n')
	print("Rules:\n1).King,Queen and Jack each will carry 10 points\n\n2).Ace can carry value of 1 or 11 which ever is ideal.\n\n3).Who ever Player or Dealer is nearer to 21 or equal to 21 wins the round.\n\n4).Player can either hit or stay after player decides to stay dealer keeps on hitting till the total reaches above 17.\n")
p1.player_name = input('Please Enter your name: ')


def replay():
	game_no = 1
	print(f'Game Number: {game_no}')
	print(f"Name = {p1.player_name}.\nPlayer's cards = {list(p1.ipcards.keys())}\n\nDealer's Cards = {list(dealer.idcards.keys())}\n")
	
		
	c = input('Do you want to Play another round?(Y/N)')		
		
	if c == 'Y' or c== 'y':

		game_no+=1
		
		p1.player_points = 0
		p1.ipcards = {}
		dealer.dealer_points = 0
		dealer.idcards = {}
		
		game()

	elif c=='N' or c == 'n':
		exit()
	else:
		print('Please choose a valid option!')
		replay()



def win_or_lose():
	if (p1.player_points<21 and p1.player_points>dealer.dealer_points) or p1.player_points == 21 or (dealer.dealer_points > 21 and p1.player_points < 21):
		print(f'Congratulations You won ${p1.bet}\n\n')
		p1.balance += p1.bet
		replay()
	elif p1.player_points == dealer.dealer_points:
		print("It's a draw! win or lose")
		replay()
	elif p1.player_points < dealer.dealer_points:
		print('Better Luck next time\n\n')
		p1.balance -= p1.bet
		
		replay()

def game():
	
	try: 
		while True:
			try:
				if p1.balance == 0:
					print('You Lost all your money!\n\n\n')
					exit()
				print(f'Your current balance is ${p1.balance}\n')
				p1.bet = int(input('Place your bet: '))
				if p1.bet > p1.balance or p1.balance < 0:
					print('Insufficient balance!\n')
					continue
			except ValueError:	
					print('Please Enter A valid Bet! (In Digits)\n\n')
					continue
			
			print('Dealers cards:')
			dealer.DF2C()
			
			print(f"{p1.player_name} your turn: ")
			p1.F2C()
			p1.hit_or_stay()
			if p1.player_points == 21:
				print(f'Congratulations You won ${p1.bet}\n')
				p1.balance += p1.bet
				
				replay()

			elif p1.player_points > 21:
				print('Better luck Next time')
				p1.balance -= p1.bet
				replay()

			elif p1.player_points == dealer.dealer_points:
				print("It's a draw!")
				replay()

			print('Now Displaying dealers remaining Cards:\n')
			
			print(list(dealer.idcards.keys()))
			dealer.hit()
			win_or_lose()
	except KeyboardInterrupt:
		exit()

display()
game()

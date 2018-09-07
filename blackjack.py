import random
class Player(object):
	def __init__(self,bankroll=1000,bet=0,win=0):
		self.bankroll=bankroll
		self.bet=bet
		self.win=win
	def ShowDetails(self):
		print('You have: '+str(self.bankroll)+' balance,'+str(self.bet)+' bet,'+str(self.win)+' win')
	def SetValues(self,sinput1,identifier):
		if identifier=='w':
			self.bankroll=self.bankroll+(int(sinput1)*2)
			self.win=int(sinput1)+int(sinput1)
			self.bet=0
		elif identifier=='l':
			#self.bankroll=self.bankroll-(int(sinput1))
			self.win=int(sinput1)-int(sinput1)
			self.bet=0
		elif identifier=='b':
			self.bankroll=self.bankroll+(int(sinput1)*2.5)
			self.win=int(sinput1)+(int(sinput1)*1.5)
			self.bet=0
		elif identifier=='p':
			self.bankroll=self.bankroll+(int(sinput1))
			self.win=0
		else:
			self.bankroll=self.bankroll-int(sinput1)
			self.bet=int(sinput1)
class Deck(object):
	def GetRandomCards(self):
		
		rank = random.choice( ('1','2','3','4','5','6','7','8','9','10','J','Q','K') )
		suit = random.choice( ('Club','Diamond','Heart','Spade') )
		if rank=='J':
			card = 'Jack of '+suit #display
		elif rank=='Q':
			card='Queen of '+suit #display
		elif rank=='K':
			card='King of '+suit #display
		elif rank=='1':
			card='Ace of '+suit #display
		else:
			card = rank +' of '+suit
		return (card,'10') if rank in ('J','Q','K') else (card,rank)
	def GetMinMaxValue(self,current_sum):
		return 11+current_sum if 11+current_sum<=21 else 1+current_sum
	def CheckIfAceExists(self,lCards):
		if '1' in lCards:
			return True
		else:
			return False
class Main():
	game_on=True
	var_lost=False
	first_time=True
	
	print('Welcome to Black Jack')
	print('***********************************')
	player=Player()
	player.ShowDetails()
	while game_on:
		sum_p=0
		sum_d=0
		lPlayerCards=[]
		lDealerCards=[]
		usedAceCountDealer=False
		usedAceCountPlayer=True
		sinput1=input('Place your bet: ')
		player.SetValues(sinput1,'')
		player.ShowDetails()
		deck=Deck()
		
		while sum_p<=21:
			if first_time:
				card_1_player,rank_player=deck.GetRandomCards()
				card_2_player,rank_2_player=deck.GetRandomCards()
				lPlayerCards.insert(0,rank_player)
				lPlayerCards.insert(1,rank_2_player)
				if rank_player=='1':
					sum_p=deck.GetMinMaxValue(int(rank_2_player))
				elif rank_2_player=='1':
					sum_p=deck.GetMinMaxValue(int(rank_player))
				else:
					sum_p=(int(rank_player)+int(rank_2_player))
				print("You have card 1 as :"+card_1_player+" and card 2 as :"+card_2_player)
				print("Sum is :"+str(sum_p))
				card_1_dealer,rank_dealer=deck.GetRandomCards()
				lDealerCards.insert(0,rank_dealer)
				if rank_dealer=='1':
					sum_d=deck.GetMinMaxValue(sum_d)
				else:
					sum_d=int(rank_dealer)
				#sum_d=int(rank_dealer)
				print("Dealer has card as :"+card_1_dealer)
				print("Sum is :"+str(sum_d))
				first_time=False
			else:
				#while soption!='h' and soption!='s':
				soption=input('Do you want to Hit or Stay ? h ,s: ')
				if soption=='h':
					card_1_player,rank_player=deck.GetRandomCards()
					lPlayerCards.append(rank_player)
					if deck.CheckIfAceExists(lPlayerCards):
						sum_p=sum_p+int(rank_player)
						if sum_p>21 and usedAceCountPlayer==False:
							sum_p=sum_p-10
							usedAceCountPlayer=True
					else:	
						if rank_player=='1':
							sum_p=deck.GetMinMaxValue(sum_p)
						else:
							sum_p=sum_p+int(rank_player)
					print("You have card  as :"+card_1_player)
					print("Sum is :"+str(sum_p))
				else:		
					break
		if sum_p>21:
			print("Bust")
			player.SetValues(sinput1,'l')
			player.ShowDetails()
			first_time=True
		elif sum_p==21 and sum_p>sum_d:
			print("Black Jack")
			player.SetValues(sinput1,'b')
			player.ShowDetails()
			first_time=True
		else:
			#if(soption=='h'):
			while sum_d<17:
				card_1_dealer,rank_dealer=deck.GetRandomCards()
				lDealerCards.append(rank_dealer)
				if deck.CheckIfAceExists(lDealerCards):
					sum_d=sum_d+int(rank_player)
					if sum_d>21 and usedAceCountDealer==False:
						sum_d=sum_d-10
						usedAceCountDealer=True
				else:
					if rank_dealer=='1':
						sum_d=deck.GetMinMaxValue(sum_d)
						
					else:
						sum_d=sum_d+int(rank_dealer)
				#sum_d=sum_d+int(rank_dealer)
				print("Dealer has card as :"+card_1_dealer)
				print("Sum is :"+str(sum_d))
			if sum_d>21:
				print("Win")
				player.SetValues(sinput1,'w')
				player.ShowDetails()
				first_time=True
			else:
				if sum_d>=17 and sum_d<=21 and sum_d<sum_p:
					print("Win")
					player.SetValues(sinput1,'w')
					player.ShowDetails()
					first_time=True
				elif sum_d==sum_p:
					print ("Push")
					player.SetValues(sinput1,'p')
					player.ShowDetails()
					first_time=True
				else:
					print("Bust")
					player.SetValues(sinput1,'l')
					player.ShowDetails()
					first_time=True
		if player.bankroll<=0:
			print('Game Over')
			game_on=False
#for shuffling deck
from random import shuffle

#to involve 2 players
from player import *

class Deck:
	def __init__(self):
		self.suits = ['d','h','c','s']
		self.faces = [1,2,3]
		self.deck = []
		self.draw = []
		self.discard = []
		self.seq = []
		
		#Generates deck
		for i in range(len(self.suits)):
			suit = self.suits[i]
			for j in range(len(self.faces)):
				num = self.faces[j]
		        	self.deck.append((suit,num))
		
		#calculates all valid sequences based on deck
		#For same number:
		x = len(self.deck)
		y = []
		for j in range(len(self.faces)):
			y.append(j)

		#1110
		for i in y:
			a = [0]*x
			a[int(0+i)] = 1
			a[int((x/4)+i)] = 1
			a[int((x/2)+i)] = 1
			self.seq.append(a)
		#0111
		for i in y:
			a = [0]*x
			a[int((x/4)+i)] = 1
			a[int((x/2)+i)] = 1
			a[int(((3*x)/4)+i)] = 1
			self.seq.append(a)
		#1011
		for i in y:
			a = [0]*x
			a[int(0+i)] = 1
			a[int((x/2)+i)] = 1
			a[int(((3*x)/4)+i)] = 1
			self.seq.append(a)
		#1101
		for i in y:
			a = [0]*x
			a[int(0+i)] = 1
			a[int((x/4)+i)] = 1
			a[int(((3*x)/4)+i)] = 1
			self.seq.append(a)










		#For same suit:
		lister = [0, int((len(self.deck)/4)), int((len(self.deck)/2)), int((3*len(self.deck)/4)), int(len(self.deck))]
		list1 = []
		list2 = []
		list3 = []
		list4 = []
		for i in range(lister[0],lister[1]):
			list1.append(i)
		for i in range(lister[1],lister[2]):
			list2.append(i)			
		for i in range(lister[2],lister[3]):
			list3.append(i)
		for i in range(lister[3],lister[4]):
			list4.append(i)
		list1 = list(reversed(list1))			
		list2 = list(reversed(list2))
		list3 = list(reversed(list3))
		list4 = list(reversed(list4))
		for i in list1:
			for self.deck[i] in self.deck:
				if i-1 >= min(list1) and i-2 >= min(list1):
					temp = [0]*len(self.deck)
					temp[i] = 1
					temp[i-1] = 1
					temp[i-2] = 1
					if temp not in self.seq:
						self.seq.append(temp)
		for i in list2:
			for self.deck[i] in self.deck:
				if i-1 >= min(list2) and i-2 >= min(list2):
					temp = [0]*len(self.deck)
					temp[i] = 1
					temp[i-1] = 1
					temp[i-2] = 1
					if temp not in self.seq:
						self.seq.append(temp)
		for i in list3:
			for self.deck[i] in self.deck:
				if i-1 >= min(list3) and i-2 >= min(list3):
					temp = [0]*len(self.deck)
					temp[i] = 1
					temp[i-1] = 1
					temp[i-2] = 1
					if temp not in self.seq:
						self.seq.append(temp)
		for i in list4:
			for self.deck[i] in self.deck:
				if i-1 >= min(list4) and i-2 >= min(list4):
					temp = [0]*len(self.deck)
					temp[i] = 1
					temp[i-1] = 1
					temp[i-2] = 1
					if temp not in self.seq:
						self.seq.append(temp)



























		
		
		#initialise two players with empty hand and knowledge initialised to 0 for all cards
		player1 = Player(self.deck)
		player2 = Player(self.deck)

		#shuffles deck
		shuffle(self.deck)

		#assigns cards to 2 players
		for i in self.deck:
			j = self.deck.index(i)
			total = len(self.suits) * len(self.faces)
			if j < (total/2):
				if j%2==0:
					player1.hand.append(i)
				else:
					player2.hand.append(i)
			elif j > (total/2 - 1) and j < (total - 1):
				self.draw.append(i)
			else:
				self.discard.append(i)

		print self.deck
		print self.seq
		print len(self.seq)


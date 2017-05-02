import numpy as np

import random

import Levenshtein

import copy

class Player1:
	def __init__(self, deck):
		self.hand = []
		self.kb = dict()
		self.reversekb = dict()
		self.binhand = [0]*len(deck)
		self.hand_str = str(0)
		self.levenlist = []

		self.priority1 = []
		self.closest1 = []
		self.pickup1 = []
		self.drop1 = []
		
		self.levenlistcopy = []

		self.win = False
		
		self.oppHand = [9]*len(deck) #9 indicates no info about it, 1 indicates it is in opponents hand, 0 indicates it is in your own hand or on discard pile
		

		#The knowledge base keeps track of the list index which represents each card
		indexes = list(range(len(deck)))
		self.kb = dict(zip(deck,indexes))
		self.reversekb = {v: k for k, v in self.kb.items()}

	def playTurn1(self, deck, discard, draw, seq, binstr, oppPick):
		self.converter(deck)
		self.levendist(binstr)
		self.pick(seq, discard, draw)
		self.converter(deck)
		self.levendist(binstr)
		self.predictAfterOppMove(oppPick, discard, seq, deck)
		self.drop(seq, discard)
		self.converter(deck)
		self.levendist(binstr)
		if 0 in self.levenlist:
			return True
		else:
			return False


		
		

	def converter(self, deck):
		self.binhand = [0]*len(deck)
		for i in self.hand:
			x = self.kb.get(i)
			self.binhand[x] = 1
		self.hand_str = ''.join(map(str, self.binhand))

	def levendist(self, binstr):
		self.levenlist = []	
		for i in range(len(binstr)):
			temp = binstr[i]
			a = Levenshtein.distance(temp, self.hand_str)
			self.levenlist.append(a)
		return self.levenlist

	def pick(self, seq, discard, draw):
		self.priority1 = []
		self.closest1 = []
		self.pickup1 = []

		self.levenlistcopy = copy.deepcopy(self.levenlist)
		for i in range(len(self.levenlistcopy)):
			if self.levenlistcopy[i] == min(self.levenlistcopy):
				self.priority1.append(i)
		for i in self.priority1:
			self.closest1.append(seq[i])

		for i in self.closest1:
			for j in range(len(self.binhand)):
				if self.binhand[j] != i[j]:
					if self.binhand[j] == 0 and i[j] ==1:
						card = self.reversekb.get(j)
						self.pickup1.append(card)
	#This strategy is very conservative and only checks in pickup1, i.e., only for the minimum distance sequences
		z = discard[-1]
		if z in self.pickup1:
			self.hand.append(z)
			discard.remove(discard[-1])
		else:
			z = draw[-1]
			self.hand.append(z)
			draw.remove(draw[-1])




				
	def predictAfterOppMove(self, oppPick, discard, seq, deck):
		self.oppHand = [9]*len(deck)

		#generates opponent hand
		for i in self.hand:
			x = self.kb.get(i)
			self.oppHand[x] = 0
		if discard:
			for i in discard:
				x = self.kb.get(i)
				self.oppHand[x] = 0
		if oppPick:
			x = self.kb.get(oppPick[0])
			self.oppHand[x] = 1

		#generates all sequences according to hand info
		self.oppSeq = copy.deepcopy(seq)
		for i in seq:
			for j in range(len(self.oppHand)):
				if i[j] == 1 and self.oppHand[j] == 0:
					self.oppSeq.remove(i)
					j = 0
					break

		self.predictedCard = []	
			
		for i in self.oppSeq:
			for j in range(len(i)):
				if i[j] == 1:
					card = self.reversekb.get(j)
					if card not in self.predictedCard:
						self.predictedCard.append(card)
		

	def drop(self, seq, discard):
		self.priority1 = []
		self.closest1 = []
		self.drop1 = []

		if 1 in self.levenlist:
			x = self.levenlist.index(1)
			target = seq[x]
			for i in range(len(self.binhand)):
				if self.binhand[i]==1 and target[i]==0:
					card = self.reversekb.get(i)
					self.hand.remove(card)
					discard.append(card)
		else:
			self.levenlistcopy = copy.deepcopy(self.levenlist)
			minLeven = min(self.levenlistcopy)
			for i in range(len(self.levenlistcopy)):
				if self.levenlistcopy[i] == min(self.levenlistcopy):
					self.priority1.append(i)
			for i in self.priority1:
				self.closest1.append(seq[i])
		
			for i in self.closest1:
				for j in range(len(self.binhand)):
					if self.binhand[j] != i[j]:
						if self.binhand[j] == 1 and i[j] == 0:
							card = self.reversekb.get(j)
							self.drop1.append(card)
			
			#This strategy is very conservative and only checks in drop1, i.e., only for the minimum distance sequences
			z = random.sample(self.drop1, 1)
			self.hand.remove(z[0])
			discard.append(z[0])
		
		


import numpy as np

import random

import Levenshtein

import copy

class Player:
	def __init__(self, deck):
		self.hand = []
		self.kb = dict()
		self.reversekb = dict()
		self.binhand = [0]*len(deck)
		self.hand_str = str(0)
		self.levenlist = []

		self.priority1 = []
		self.priority2 = []
		self.priority3 = []
		self.priority4 = []
		self.closest1 = []
		self.closest2 = []
		self.closest3 = []
		self.closest4 = []

		self.pickup1 = []
		self.pickup2 = []
		self.pickup3 = []
		self.pickup4 = []
		self.drop1 = []
		self.drop2 = []
		self.drop3 = []
		self.drop4 = []
		
		self.levenlistcopy = []

		self.win = False
		

		#The knowledge base keeps track of the list index which represents each card
		indexes = list(range(len(deck)))
		self.kb = dict(zip(deck,indexes))
		self.reversekb = {v: k for k, v in self.kb.items()}

	def playTurn(self, deck, discard, draw, seq, binstr):
		self.converter(deck)
		self.levendist(binstr)
		self.pick(seq, discard, draw)
		self.converter(deck)
		self.levendist(binstr)
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
		self.priority2 = []
		self.priority3 = []
		self.priority4 = []
		self.closest1 = []
		self.closest2 = []
		self.closest3 = []
		self.closest4 = []
		self.pickup1 = []
		self.pickup2 = []
		self.pickup3 = []
		self.pickup4 = []

		self.levenlistcopy = copy.deepcopy(self.levenlist)
		for i in range(len(self.levenlistcopy)):
			if self.levenlistcopy[i] == min(self.levenlistcopy):
				self.priority1.append(i)
		for i in self.priority1:
			self.closest1.append(seq[i])
		for i in self.priority1:
			self.levenlistcopy[i] = 1000

		for i in range(len(self.levenlistcopy)):
			if self.levenlistcopy[i] == min(self.levenlistcopy):
				self.priority2.append(i)
		for i in self.priority2:
			self.closest2.append(seq[i])
		for i in self.priority2:
			self.levenlistcopy[i] = 1000

		for i in range(len(self.levenlistcopy)):
			if self.levenlistcopy[i] == min(self.levenlistcopy):
				self.priority3.append(i)
		for i in self.priority3:
			self.closest3.append(seq[i])

		for i in range(len(self.levenlistcopy)):
			if i not in self.priority1 and i not in self.priority2 and i not in self.priority3:
				self.priority4.append(i)
		for i in self.priority4:
			self.closest4.append(seq[i])

		for i in self.closest1:
			for j in range(len(self.binhand)):
				if self.binhand[j] != i[j]:
					if self.binhand[j] == 0 and i[j] ==1:
						card = self.reversekb.get(j)
						self.pickup1.append(card)

		for i in self.closest2:
			for j in range(len(self.binhand)):
				if self.binhand[j] != i[j]:
					if self.binhand[j] == 0 and i[j] ==1:
						card = self.reversekb.get(j)
						self.pickup2.append(card)

		for i in self.closest3:
			for j in range(len(self.binhand)):
				if self.binhand[j] != i[j]:
					if self.binhand[j] == 0 and i[j] ==1:
						card = self.reversekb.get(j)
						self.pickup3.append(card)
		for i in self.closest4:
			for j in range(len(self.binhand)):
				if self.binhand[j] != i[j]:
					if self.binhand[j] == 0 and i[j] ==1:
						card = self.reversekb.get(j)
						self.pickup4.append(card)

	#This strategy is very conservative and only checks in pickup1, i.e., only for the minimum distance sequences
		z = discard[-1]
		if z in self.pickup1:
			self.hand.append(z)
			discard.remove(discard[-1])
		else:
			z = draw[-1]
			self.hand.append(z)
			draw.remove(draw[-1])

	def drop(self, seq, discard):
		self.priority1 = []
		self.priority2 = []
		self.priority3 = []
		self.priority4 = []
		self.closest1 = []
		self.closest2 = []
		self.closest3 = []
		self.closest4 = []
		self.drop1 = []
		self.drop2 = []
		self.drop3 = []
		self.drop4 = []

		self.levenlistcopy = copy.deepcopy(self.levenlist)
		minLeven = min(self.levenlistcopy)
		for i in range(len(self.levenlistcopy)):
			if self.levenlistcopy[i] == min(self.levenlistcopy):
				self.priority1.append(i)
		for i in self.priority1:
			self.closest1.append(seq[i])
		for i in self.priority1:
			self.levenlistcopy[i] = 1000

		for i in range(len(self.levenlistcopy)):
			if self.levenlistcopy[i] == min(self.levenlistcopy):
				self.priority2.append(i)
		for i in self.priority2:
			self.closest2.append(seq[i])
		for i in self.priority2:
			self.levenlistcopy[i] = 1000

		for i in range(len(self.levenlistcopy)):
			if self.levenlistcopy[i] == min(self.levenlistcopy):
				self.priority3.append(i)
		for i in self.priority3:
			self.closest3.append(seq[i])

		for i in range(len(self.levenlistcopy)):
			if i not in self.priority1 and i not in self.priority2 and i not in self.priority3:
				self.priority4.append(i)
		for i in self.priority4:
			self.closest4.append(seq[i])

		for i in self.closest1:
			for j in range(len(self.binhand)):
				if self.binhand[j] != i[j]:
					if self.binhand[j] == 1 and i[j] == 0:
						card = self.reversekb.get(j)
						self.drop1.append(card)

		for i in self.closest2:
			for j in range(len(self.binhand)):
				if self.binhand[j] != i[j]:
					if self.binhand[j] == 1 and i[j] == 0:
						card = self.reversekb.get(j)
						self.drop2.append(card)

		for i in self.closest3:
			for j in range(len(self.binhand)):
				if self.binhand[j] != i[j]:
					if self.binhand[j] == 1 and i[j] == 0:
						card = self.reversekb.get(j)
						self.drop3.append(card)
		for i in self.closest4:
			for j in range(len(self.binhand)):
				if self.binhand[j] != i[j]:
					if self.binhand[j] == 1 and i[j] == 0:
						card = self.reversekb.get(j)
						self.drop4.append(card)
		
		
		
		#This strategy is very conservative and only checks in drop1, i.e., only for the minimum distance sequences
		z = random.sample(self.drop1, 1)
		self.hand.remove(z[0])
		discard.append(z[0])

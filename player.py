import numpy as np

import random

import Levenshtein

import copy

class Player:
	def __init__(self, deck):
		self.hand = []
		self.kb = dict()
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
		self.restclosest = []

		self.pickup1 = []
		self.pickup2 = []
		self.pickup3 = []
		self.drop1 = []
		self.drop2 = []
		self.drop3 = []
		self.restpickup = []
		self.restdrop = []
		
		self.levenlistcopy = []
		

		#The knowledge base keeps track of the list index which represents each card
		indexes = list(range(len(deck)))
		self.kb = dict(zip(deck,indexes))

	#takes the hand of the player and outputs a list with updated binary values for cards in hand; also converts it into binary string form
	def converter(self, hand):
		for i in hand:
			x = self.kb.get(i)
			self.binhand[x] = 1
		self.hand_str = ''.join(map(str, self.binhand))

	def levendist(self, binstr):	
		for i in range(len(binstr)):
			temp = binstr[i]
			a = Levenshtein.distance(temp, self.hand_str)
			self.levenlist.append(a)
		
	def priority(self, seq):
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
			self.restclosest.append(seq[i])

		#We have the lists of the indexes, now converting them into pick and drop card lists
		temp1pick = []
		temp1drop = []
		for i in self.closest1:
			for x in range(len(self.closest1)):
				if i[x] != self.binhand[x]:
					if i[x] == 0 and self.binhand[x] == 1:
						temp1drop.append(x)
					elif i[x] == 1 and self.binhand[x] == 0:
						temp1pick.append(x)
		self.pickup1 = temp1pick
		self.drop1 = temp1drop

		
	
			

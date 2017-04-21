import numpy as np

import random

import Levenshtein

class Player:
	def __init__(self, deck):
		self.hand = []
		self.kb = dict()
		self.binhand = [0]*len(deck)
		self.handstr = str(0)

		#The knowledge base keeps track of the list index which represents each card
		indexes = list(range(len(deck)))
		self.kb = dict(zip(deck,indexes))

	#takes the hand of the player and outputs a list with updated binary values for cards in hand
	def converter(self, hand):
		for i in hand:
			x = self.kb.get(i)
			self.binhand[x] = 1

	def levendist(self, binstr, hand):
		self.hand_str = ''.join(map(str, hand))
		print self.hand_str

	
			

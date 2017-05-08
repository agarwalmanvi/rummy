from deck import *

winninglist = []

i = 0

while i<100:
	rummy = Deck()
	winner = rummy.winplay
	winninglist.append(winner)
	i = i + 1
	
print winninglist

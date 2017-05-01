from deck import *

winninglist = []

i = 0

while i<100:
	rummy = Deck()
	winner = rummy.winplay
	winninglist.append(winner)
	print i, winner
	i = i + 1
	
print 'Games won by 0'
print winninglist.count(0)
print 'Games won by 1'
print winninglist.count(1)
print 'Inconclusive games'
print winninglist.count(2)

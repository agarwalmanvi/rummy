from deck import *
from multiprocessing import Pool

def execute_game(i):
        print "Running game : ", i 
	rummy = Deck()
	winner = rummy.winplay
	print i, winner
        return winner	

winninglist = []
indices = list(xrange(100))

pool = Pool(4)
winninglist.append((pool.map(execute_game, indices)))

winninglist = winninglist[0]
print 'Games won by 0'
print winninglist.count(0)
print 'Games won by 1'
print winninglist.count(1)
print 'Inconclusive games'
print winninglist.count(2)

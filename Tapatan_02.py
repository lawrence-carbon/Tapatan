#new
from collections import deque


class Peca:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, player, idPeca, initX, initY):

        self.IDplayer = player
        self.IDpeca = idPeca
        self.posX = initX
        self.posY = initY

    def getX(self):
        return self.posX

    def getY(self):
        return self.posY


p = Peca(1,2,3,4)

peca_default= Peca(0,0,0,0)
#pecas jogador 1
j1p1ini=Peca(1,1,0,0)
j1p2ini=Peca(1,2,2,0)
j1p3ini=Peca(1,3,2,1)
#pecas jogador 2
j2p1ini=Peca(2,1,1,0)
j2p2ini=Peca(2,2,0,2)
j2p3ini=Peca(2,3,2,2)

#monta fila de pecas para inicializar o tabuleiro
filaPecas=[j1p1ini,j1p2ini,j1p3ini,j2p1ini,j2p2ini,j2p3ini]

board = [1,2,1,
		 0,0,0,
		 2,1,2]

def printTable():
    print '   ',board[0],' | ', board[1],' | ', board[2]
    print '    --------------'
    print '   ',board[3],' | ', board[4],' | ', board[5]
    print '    --------------'
    print '   ',board[6],' | ', board[7],' | ', board[8]


printTable()







print 'fim de execucao'

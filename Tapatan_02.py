#new

class Peca:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.posX = initX
        self.posY = initY

    def getX(self):
        return self.posX

    def getY(self):
        return self.posY


p = Peca(7,6)
i = Peca(3,2)

print(p.getX())
print(p.getY())

print(i.getX())
print(i.getY())

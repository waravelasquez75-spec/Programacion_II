import math
class MiPunto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distancia(self, *args):
        if len(args) == 1:
            otro = args[0]
            return math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)
        else:
            return math.sqrt((self.x - args[0])**2 + (self.y - args[1])**2)
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
p1 = MiPunto()
p2 = MiPunto(10, 30.5)
print("Punto 1:", p1)
print("Punto 2:", p2)
print("Distancia entre puntos:", p1.distancia(p2))
print("Distancia con coordenadas:", p1.distancia(10, 30.5))
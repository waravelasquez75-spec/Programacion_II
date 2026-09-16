import math
class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, otro):
        return AlgebraVectorial(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    def __mul__(self, r):
        return AlgebraVectorial(self.x * r, self.y * r, self.z * r)
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def normal(self):
        lon = self.longitud()
        if lon == 0:
            return AlgebraVectorial(0, 0, 0)
        return AlgebraVectorial(self.x/lon, self.y/lon, self.z/lon)
    def productoEscalar(self, otro):
        return self.x*otro.x + self.y*otro.y + self.z*otro.z
    def productoVectorial(self, otro):
        return AlgebraVectorial(
            self.y*otro.z - self.z*otro.y,
            self.z*otro.x - self.x*otro.z,
            self.x*otro.y - self.y*otro.x
        )
    def perpendicular(self, otro, tipo=1):
        if tipo == 1:
            suma = self + otro
            resta = AlgebraVectorial(self.x - otro.x, self.y - otro.y, self.z - otro.z)
            return abs(suma.longitud() - resta.longitud()) < 0.000001
        if tipo == 3:
            return abs(self.productoEscalar(otro)) < 0.000001
        if tipo == 4:
            suma = self + otro
            return abs(suma.longitud()**2 - (self.longitud()**2 + otro.longitud()**2)) < 0.000001
        return False
    def paralela(self, otro, tipo=1):
        if tipo == 1:
            if otro.x == 0 and otro.y == 0 and otro.z == 0:
                return False
            return abs(self.x*otro.y - self.y*otro.x) < 0.000001 and abs(self.x*otro.z - self.z*otro.x) < 0.000001
        if tipo == 2:
            cruz = self.productoVectorial(otro)
            return abs(cruz.x) < 0.000001 and abs(cruz.y) < 0.000001 and abs(cruz.z) < 0.000001
        return False
    def proyeccion(self, b):
        escalar = self.productoEscalar(b) / (b.longitud() ** 2)
        return b * escalar
    def componente(self, b):
        return self.productoEscalar(b) / b.longitud()
a = AlgebraVectorial(1, 0, 0)
b = AlgebraVectorial(0, 1, 0)
print("a =", a)
print("b =", b)
print("suma =", a + b)
print("2 * a =", a * 2)
print("longitud a =", a.longitud())
print("perpendicular (tipo 3) =", a.perpendicular(b, 3))
print("paralela (tipo 2) =", a.paralela(b, 2))
print("proyeccion =", a.proyeccion(b))
print("componente =", a.componente(b))

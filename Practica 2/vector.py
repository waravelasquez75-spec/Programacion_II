import math
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    def __mul__(self, r):
        return Vector(self.x * r, self.y * r, self.z * r)
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def normal(self):
        lon = self.longitud()
        if lon == 0:
            return Vector(0, 0, 0)
        return Vector(self.x/lon, self.y/lon, self.z/lon)
    def __matmul__(self, otro):
        return self.x*otro.x + self.y*otro.y + self.z*otro.z
    def cruz(self, otro):
        return Vector(
            self.y*otro.z - self.z*otro.y,
            self.z*otro.x - self.x*otro.z,
            self.x*otro.y - self.y*otro.x
        )
a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
print("a =", a)
print("b =", b)
print("suma =", a + b)
print("2 * a =", a * 2)
print("longitud a =", a.longitud())
print("normal a =", a.normal())
print("producto escalar =", a @ b)
print("producto vectorial =", a.cruz(b))
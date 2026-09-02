class Estadistica:
    def __init__(self, nums):
        self.nums = nums
    def promedio(self):
        return sum(self.nums) / len(self.nums)
    def desviacion(self):
        prom = self.promedio()
        suma = 0
        for x in self.nums:
            suma += (x - prom) ** 2
        return (suma / (len(self.nums) - 1)) ** 0.5
entrada = input("Ingrese 10 números: ").split()
nums = list(map(float, entrada))
est = Estadistica(nums)
print(f"El promedio es {est.promedio():.2f}")
print(f"La desviación estandar es {est.desviacion():.5f}")
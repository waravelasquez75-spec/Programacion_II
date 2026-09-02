import time
import random
class Cronometro:
    def __init__(self):
        self.inici = time.time() * 1000
        self.finaliza = 0
    def get_inicia(self):
        return self.inicia
    def get_finaliza(self):
        return self.finaliza
    def inicia(self):
        self.inicia = time.time() * 1000
    def detener(self):
        self.finaliza = time.time() * 1000
    def lapsoDeTiempo(self):
        return self.finaliza - self.inicia
def ordenar_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
crono = Cronometro()
numeros = [random.randint(1, 1000000) for _ in range(100000)]
print("Ordenando 100.000 números espera un momento")
crono.inicia()
ordenar_seleccion(numeros)
crono.detener()
print("Tiempo de ordenación:", round(crono.lapsoDeTiempo(), 2), "ms")
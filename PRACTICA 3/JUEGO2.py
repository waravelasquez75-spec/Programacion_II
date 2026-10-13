import random
class Juego:
    def __init__(self, numero_de_vidas: int):
        self.vidas_iniciales = numero_de_vidas
        self.numero_de_vidas = numero_de_vidas
        self.record = 0
    def reinicia_partida(self):
        self.numero_de_vidas = self.vidas_iniciales
    def actualiza_record(self):
        if self.numero_de_vidas > self.record:
            self.record = self.numero_de_vidas
            print(f"¡Nuevo récord! Vidas restantes: {self.record}")
        else:
            print(f"Récord actual: {self.record}")
    def quita_vida(self) -> bool:
        self.numero_de_vidas -= 1
        if self.numero_de_vidas > 0:
            print(f"Te quedan {self.numero_de_vidas} vidas.")
            return True
        else:
            print("¡No te quedan más vidas! Game Over.")
            return False
class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas: int):
        super().__init__(numero_de_vidas)
        self.numero_a_adivinar = 0
    def valida_numero(self, numero: int) -> bool:
        return 0 <= numero <= 10
    def juega(self):
        self.reinicia_partida()
        self.numero_a_adivinar = random.randint(0, 10)
        print(f"\n=== {self.__class__.__name__} ===")
        print(f"Tienes {self.numero_de_vidas} vidas.")
        print("Adivina un número entre 0 y 10.")
        while True:
            try:
                intento = int(input("Ingresa tu número: "))
            except ValueError:
                print("Por favor ingresa un número entero.")
                continue
            if not self.valida_numero(intento):
                print("Número no válido. Intenta de nuevo.")
                continue
            if intento == self.numero_a_adivinar:
                print("¡Acertaste!!")
                self.actualiza_record()
                break
            else:
                quedan_vidas = self.quita_vida()
                if quedan_vidas:
                    if intento < self.numero_a_adivinar:
                        print("El número a adivinar es MAYOR.")
                    else:
                        print("El número a adivinar es MENOR.")
                    print("Inténtalo de nuevo.")
                else:
                    print(f"El número era: {self.numero_a_adivinar}")
                    break
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def valida_numero(self, numero: int) -> bool:
        if not (0 <= numero <= 10):
            print("Error: el número debe estar entre 0 y 10.")
            return False
        if numero % 2 != 0:
            print("Error: el número debe ser PAR.")
            return False
        return True
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def valida_numero(self, numero: int) -> bool:
        if not (0 <= numero <= 10):
            print("Error: el número debe estar entre 0 y 10.")
            return False
        if numero % 2 == 0:
            print("Error: el número debe ser IMPAR.")
            return False
        return True
if __name__ == "__main__":
    print("========== INICIANDO LOS TRES JUEGOS ==========")
    juego_normal = JuegoAdivinaNumero(3)
    juego_normal.juega()
    juego_par = JuegoAdivinaPar(3)
    juego_par.juega()
    juego_impar = JuegoAdivinaImpar(3)
    juego_impar.juega()
    print("\n========== FIN DE LOS JUEGOS ==========")
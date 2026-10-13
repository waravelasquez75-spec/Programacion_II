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
    def juega(self):
        self.reinicia_partida()
        self.numero_a_adivinar = random.randint(0, 10)
        print("\n=== Juego Adivina el Número (0-10) ===")
        print(f"Tienes {self.numero_de_vidas} vidas.")
        while True:
            try:
                intento = int(input("Adivina un número entre 0 y 10: "))
            except ValueError:
                print("Por favor ingresa un número entero.")
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
if __name__ == "__main__":  
    juego = JuegoAdivinaNumero(3)
    juego.juega()
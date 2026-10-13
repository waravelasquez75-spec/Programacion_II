class Sensor:
    tipo = "Genérico"          # atributo de CLASE
    def __init__(self, id: str, **kwargs):
        self.id = id           # atributo de INSTANCIA
        self.encendido = False # atributo de INSTANCIA
        super().__init__(**kwargs)
    def activar(self):
        self.encendido = True
        print(f"[{self.tipo}] Sensor {self.id} ACTIVADO")
    def desactivar(self):
        self.encendido = False
        print(f"[{self.tipo}] Sensor {self.id} DESACTIVADO")
    def __str__(self):
        estado = "ENCENDIDO" if self.encendido else "APAGADO"
        return f"Sensor(tipo={self.tipo}, id={self.id}, estado={estado})"
class Camara(Sensor):
    tipo = "Cámara"            # atributo de CLASE
    def __init__(self, id: str, resolucion: str, **kwargs):
        self.resolucion = resolucion  # atributo de INSTANCIA
        super().__init__(id=id, **kwargs)
    def __str__(self):
        base = super().__str__()
        return f"{base}, resolucion={self.resolucion}"
class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"         # atributo de CLAS
    def __init__(self, id: str, alcance: int, **kwargs):
        self.alcance = alcance # atributo de INSTANCIA
        super().__init__(id=id, **kwargs)
    def __str__(self):
        base = super().__str__()
        return f"{base}, alcance={self.alcance}m"
class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehiculo Autónomo" # atributo de CLASE
    def __init__(self, id: str, resolucion: str, alcance: int):
        super().__init__(id=id, resolucion=resolucion, alcance=alcance)
    def __str__(self):
        estado = "ENCENDIDO" if self.encendido else "APAGADO"
        return (f"VehiculoAutonomo(tipo={self.tipo}, id={self.id}, "
                f"resolucion={self.resolucion}, alcance={self.alcance}m, "
                f"estado={estado})")
if __name__ == "__main__":
    print("=== Sistema de Vehículo Autónomo ===\n")
    auto = VehiculoAutonomo(id="VA-001", resolucion="4K", alcance=150)
    print("1. Estado inicial:")
    print(auto)
    print()
    print("2. Activando:")
    auto.activar()
    print(auto)
    print()
    print("3. Desactivando:")
    auto.desactivar()
    print(auto)
    print()

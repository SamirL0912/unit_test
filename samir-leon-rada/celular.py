class Bateria:
    def __init__(self, capacidad):
        self.capacidad = capacidad

class Celular:
    def __init__(self, marca):
        self.marca = marca
        self.bateria = Bateria(5000)

    def obtener_capacidad_bateria(self):
        return self.bateria.capacidad

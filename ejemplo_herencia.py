class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def acelerar(self):
        print("Acelerando...")

    def frenar(self):
        print("Frenando...")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas, tipo_combustible):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas
        self.tipo_combustible = tipo_combustible



class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

class Vaca(Animal):
    def hacer_sonido(self):
        print("Muu!")

animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    animal.hacer_sonido()

class Perro():
    def __init__(self, nombre):
        self.nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


perrico = Perro("Firulais")
print(perrico.nombre)
perrico.nombre = "Firulais 2"
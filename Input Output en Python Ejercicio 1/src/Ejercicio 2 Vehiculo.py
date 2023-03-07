import pickle

class Vehículo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando...")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando...")

mi_coche = Vehículo("Ford", "Mustang", "red")

# Guardar objeto en un archivo
with open('vehiculo.pkl', 'wb') as archivo:
    pickle.dump(mi_coche, archivo)

# Cargar objeto desde un archivo
with open('vehiculo.pkl', 'rb') as archivo:
    coche_cargado = pickle.load(archivo)

# Imprimir los atributos del objeto cargado
print(coche_cargado.marca)
print(coche_cargado.modelo)
print(coche_cargado.color)


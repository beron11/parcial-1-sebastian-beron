# ventana.py

class Ventana:
    def __init__(self, tipo, dimensiones, material):
        self.tipo = tipo
        self.dimensiones = dimensiones
        self.material = material

    def __str__(self):
        return f"Ventana de {self.material}, tipo {self.tipo}, dimensiones {self.dimensiones}"

if __name__ == "__main__":
    # Prueba de la clase Ventana
    ventana = Ventana("Corrediza", "100x150cm", "Aluminio")
    print(ventana)
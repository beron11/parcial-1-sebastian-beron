# cliente.py

class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

if __name__ == "__main__":
    # Prueba de la clase Cliente
    cliente = Cliente("Juan Pérez", "Calle 123, Ciudad", "555-1234")
    print(cliente)
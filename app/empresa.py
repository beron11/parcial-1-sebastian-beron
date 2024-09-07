# empresa.py
from cotizacion import Cotizacion
from cliente import Cliente
from ventana import Ventana
from cotizacion_item import CotizacionItem

class Empresa:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def realizar_cotizacion(self, cotizacion):
        print(f"Realizando cotización:\n{cotizacion}")

    def __str__(self):
        return f"Empresa: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

if __name__ == "__main__":
    # Prueba de la clase Empresa
    empresa = Empresa("Ventanas XYZ", "Av. Principal 456, Ciudad", "555-5678")
    print(empresa)
    
    cliente = Cliente("Juan Pérez", "Calle 123, Ciudad", "555-1234")
    cotizacion = Cotizacion(cliente)
    
    ventana = Ventana("Corrediza", "100x150cm", "Aluminio")
    item = CotizacionItem(ventana, 2, 150.00)
    cotizacion.agregar_item(item)
    
    empresa.realizar_cotizacion(cotizacion)
# cotizacion.py
from datetime import date
from cliente import Cliente
from cotizacion_item import CotizacionItem
from ventana import Ventana

class Cotizacion:
    def __init__(self, cliente):
        self.fecha = date.today()
        self.cliente = cliente
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.items)

    def __str__(self):
        result = f"Cotización para {self.cliente}\nFecha: {self.fecha}\n\nItems:\n"
        for item in self.items:
            result += f"{item}\n"
        result += f"\nTotal: ${self.calcular_total():.2f}"
        return result

if __name__ == "__main__":
    # Prueba de la clase Cotizacion
    cliente = Cliente("Juan Pérez", "Calle 123, Ciudad", "555-1234")
    cotizacion = Cotizacion(cliente)
    
    ventana1 = Ventana("Corrediza", "100x150cm", "Aluminio")
    item1 = CotizacionItem(ventana1, 2, 150.00)
    cotizacion.agregar_item(item1)
    
    ventana2 = Ventana("Fija", "80x100cm", "PVC")
    item2 = CotizacionItem(ventana2, 1, 100.00)
    cotizacion.agregar_item(item2)
    
    print(cotizacion)
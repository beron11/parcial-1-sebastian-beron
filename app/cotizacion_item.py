# cotizacion_item.py
from ventana import Ventana

class CotizacionItem:
    def __init__(self, ventana, cantidad, precio_unitario):
        self.ventana = ventana
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def calcular_subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.ventana} - Cantidad: {self.cantidad}, Precio unitario: ${self.precio_unitario:.2f}, Subtotal: ${self.calcular_subtotal():.2f}"

if __name__ == "__main__":
    # Prueba de la clase CotizacionItem
    ventana = Ventana("Corrediza", "100x150cm", "Aluminio")
    item = CotizacionItem(ventana, 2, 150.00)
    print(item)
    print(f"Subtotal: ${item.calcular_subtotal():.2f}")
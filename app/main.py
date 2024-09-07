# main.py
from empresa import Empresa
from cliente import Cliente
from ventana import Ventana
from cotizacion import Cotizacion
from cotizacion_item import CotizacionItem

class SistemaCotizacion:
    def __init__(self):
        self.empresa = None

    def crear_empresa(self):
        print("\n--- Crear Nueva Empresa ---")
        nombre = input("Nombre de la empresa: ")
        direccion = input("Dirección de la empresa: ")
        telefono = input("Teléfono de la empresa: ")
        self.empresa = Empresa(nombre, direccion, telefono)
        print(f"\nEmpresa creada: {self.empresa}")

    def crear_cliente(self):
        print("\n--- Crear Nuevo Cliente ---")
        nombre = input("Nombre del cliente: ")
        direccion = input("Dirección del cliente: ")
        telefono = input("Teléfono del cliente: ")
        return Cliente(nombre, direccion, telefono)

    def crear_cotizacion(self):
        if not self.empresa:
            print("Primero debe crear una empresa.")
            return None
        
        cliente = self.crear_cliente()
        cotizacion = Cotizacion(cliente)
        
        while True:
            print("\n--- Agregar Ítem a la Cotización ---")
            tipo = input("Tipo de ventana: ")
            dimensiones = input("Dimensiones de la ventana: ")
            material = input("Material de la ventana: ")
            cantidad = int(input("Cantidad: "))
            precio_unitario = float(input("Precio unitario: "))

            ventana = Ventana(tipo, dimensiones, material)
            item = CotizacionItem(ventana, cantidad, precio_unitario)
            cotizacion.agregar_item(item)

            continuar = input("¿Agregar otro ítem? (s/n): ")
            if continuar.lower() != 's':
                break

        return cotizacion

    def realizar_cotizacion(self, cotizacion):
        if not self.empresa:
            print("Primero debe crear una empresa.")
            return
        
        self.empresa.realizar_cotizacion(cotizacion)

    def ejecutar(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Crear empresa")
            print("2. Crear nueva cotización")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_empresa()
            elif opcion == "2":
                cotizacion = self.crear_cotizacion()
                if cotizacion:
                    self.realizar_cotizacion(cotizacion)
            elif opcion == "3":
                print("Gracias por usar el sistema de cotización. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    sistema = SistemaCotizacion()
    sistema.ejecutar()
# parcial-1-sebastian-beron
cotización de ventanas pqr
# Descripción
Este proyecto, desarrollado en Python, tiene como objetivo crear un sistema de gestión para una empresa dedicada a la fabricación de ventanas en aluminio. El sistema permite gestionar información sobre clientes, cotizaciones, productos y la empresa en general.
# Autor
juan sebastian beron
# Estructura del Proyecto
cliente.py: Contiene la clase Cliente que almacena la información de los clientes (nombre, dirección, teléfono, etc.).
cotizacion_item.py: Define la clase CotizacionItem que representa un ítem individual dentro de una cotización (tipo de ventana, cantidad, precio unitario).
cotizacion.py: Implementa la clase Cotizacion que agrupa varios CotizacionItem y calcula el total de la cotización.
empresa.py: Contiene la clase Empresa que almacena información general sobre la empresa (nombre, dirección, contacto, etc.).
ventana.py: Define la clase Ventana que representa los diferentes tipos de ventanas que fabrica la empresa (corredizas, proyectantes, etc.).
main.py: Es el punto de entrada del programa, donde se crean instancias de las clases y se ejecutan las funcionalidades principales.
# Funcionalidades
Gestión de clientes: Agregar, modificar y eliminar clientes.
Creación de cotizaciones: Agregar productos a una cotización, calcular el total y generar un reporte.
Catalogo de productos: Mantener un catálogo de los diferentes tipos de ventanas.
Información de la empresa: Mostrar los datos de contacto de la empresa.
# Tecnologías Utilizadas
Python: Lenguaje de programación principal.
[Otras bibliotecas utilizadas, por ejemplo: pandas, NumPy, SQLAlchemy]
# Instrucciones de Uso
# 1.Clonar el repositorio:
Bash
git clone (https://github.com/beron11/parcial-1-sebastian-beron)
# 2.Crear un entorno virtual:
Bash
python -m venv venv
# 3.Activar el entorno virtual:
Windows: venv\Scripts\activate.

Linux/macOS: source venv/bin/activate.
# 4.Instalar las dependencias:
Bash
pip install -r requirements.txt
# 5.Ejecutar el programa:
Bash
python main.py

Requerimientos del Sistema de Cotización de Ventanas
1. Requisitos Funcionales
1.1 Gestión de Empresa

RF1.1: El sistema debe permitir crear una empresa con nombre, dirección y teléfono.
RF1.2: El sistema debe almacenar la información de la empresa para su uso en las cotizaciones.

1.2 Gestión de Clientes

RF2.1: El sistema debe permitir crear un cliente con nombre, dirección y teléfono.
RF2.2: El sistema debe asociar un cliente a cada cotización.

1.3 Gestión de Ventanas

RF3.1: El sistema debe permitir definir una ventana con tipo, dimensiones y material.
RF3.2: El sistema debe permitir incluir múltiples ventanas en una cotización.

1.4 Gestión de Cotizaciones

RF4.1: El sistema debe permitir crear una nueva cotización para un cliente.
RF4.2: El sistema debe permitir agregar múltiples ítems (ventanas) a una cotización.
RF4.3: El sistema debe calcular automáticamente el subtotal de cada ítem en la cotización.
RF4.4: El sistema debe calcular automáticamente el total de la cotización.
RF4.5: El sistema debe mostrar la fecha de creación de la cotización.

1.5 Realización de Cotizaciones

RF5.1: El sistema debe permitir a la empresa realizar una cotización.
RF5.2: El sistema debe mostrar un resumen completo de la cotización realizada.

2. Requisitos No Funcionales
2.1 Usabilidad

RNF1.1: El sistema debe proporcionar una interfaz de línea de comandos clara y fácil de usar.
RNF1.2: El sistema debe proporcionar mensajes de error claros y útiles.

2.2 Rendimiento

RNF2.1: El sistema debe responder a las entradas del usuario en menos de 1 segundo.

2.3 Confiabilidad

RNF3.1: El sistema debe manejar entradas inválidas sin bloquearse.

2.4 Portabilidad

RNF4.1: El sistema debe funcionar en cualquier plataforma que soporte Python 3.6 o superior.

2.5 Mantenibilidad

RNF5.1: El código del sistema debe estar organizado en módulos separados para cada clase principal.
RNF5.2: Cada módulo debe incluir pruebas unitarias básicas.

2.6 Escalabilidad

RNF6.1: El sistema debe ser diseñado de manera que permita fácilmente la adición de nuevas funcionalidades en el futuro.

3. Restricciones

El sistema debe ser desarrollado utilizando Python 3.6 o superior.
El sistema debe utilizar solo la biblioteca estándar de Python, sin dependencias externas.
El sistema debe funcionar en un entorno de línea de comandos.

4. Supuestos y Dependencias

Se asume que los usuarios tienen conocimientos básicos de operación de línea de comandos.
Se asume que los usuarios tienen instalado Python 3.6 o superior en sus sistemas.
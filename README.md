# Sistema básico de gestión de restaurante

## Datos del estudiante

Nombre: Nahomy Guanipatin.
Asignatura: Programación Orientada a Objetos.
Actividad: Taller práctico - Organización modular de un sistema orientado a objetos en Python.

## Descripción del proyecto

Este proyecto trata sobre un sistema básico de restaurante hecho en Python, usando Programación Orientada a Objetos.

El sistema permite registrar productos del restaurante, como platos, bebidas o entradas. También permite registrar clientes con sus datos principales. La información se muestra en la consola de manera ordenada.

La finalidad de este trabajo es practicar el uso de clases, objetos, métodos, constructores, importaciones y la organización del código en diferentes archivos.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   └── restaurante.py
├── main.py
└── README.md
```

## Explicación de los archivos

### modelos/producto.py

En este archivo se encuentra la clase `Producto`.
Esta clase representa los productos que ofrece el restaurante, como platos o bebidas. Guarda el nombre, la categoría, el precio y si el producto está disponible.

### modelos/cliente.py

En este archivo se encuentra la clase `Cliente`.
Esta clase representa a una persona que consume en el restaurante. Guarda el nombre, el teléfono y el número de mesa.

### servicios/restaurante.py

En este archivo se encuentra la clase `Restaurante`.
Esta clase se encarga de administrar los productos y clientes registrados. Permite agregar productos, agregar clientes y mostrar la información.

### main.py

Este es el archivo principal del programa.
Aquí se crean los objetos del restaurante, los productos y los clientes. También se llaman los métodos para mostrar la información en consola.

## Conceptos aplicados

En este proyecto se aplican los siguientes conceptos:

* Clases
* Objetos
* Atributos
* Métodos
* Constructor `__init__()`
* Método especial `__str__()`
* Importaciones entre archivos
* Organización modular del proyecto

## Ejecución del programa

Para ejecutar el programa, se debe abrir la terminal en la carpeta del proyecto y escribir:

```bash
py main.py
```

## Reflexión

La modularización es importante porque ayuda a tener el código más ordenado y fácil de entender.
Al separar el proyecto en varios archivos, cada clase tiene una responsabilidad diferente.

En este sistema, la clase `Producto` representa los productos del restaurante, la clase `Cliente` representa a los clientes y la clase `Restaurante` administra la información. Esto permite que el programa sea más claro y fácil de modificar.

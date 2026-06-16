# Clase que representa un producto del restaurante
class Producto:
    def __init__(self, nombre, categoria, precio, disponible=True):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # Cambia el producto a disponible
    def marcar_disponible(self):
        self.disponible = True

    # Cambia el producto a no disponible
    def marcar_no_disponible(self):
        self.disponible = False

    # Muestra los datos del producto
    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Producto: {self.nombre} | Categoria: {self.categoria} | Precio: ${self.precio:.2f} | Estado: {estado}"

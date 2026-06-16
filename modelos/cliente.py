# Clase que prepresenta a un cliente del restaurante
class Cliente:
    def __init__(self, nombre, telefono, mesa):
        self.nombre = nombre
        self.telefono = telefono
        self.mesa = mesa

    # Cambio el número de mesa del cliente
    def cambiar_mesa(self, nueva_mesa):
        self.mesa = nueva_mesa

    # Muestra los datos del cliente
    def __str__(self):
        return f"Cliente: {self.nombre} | Teléfono: {self.telefono} | Mesa: {self.mesa}"
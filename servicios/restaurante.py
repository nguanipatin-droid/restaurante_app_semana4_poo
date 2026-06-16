# Clase que administra los productos y clientes del restaurante
class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    # Agrega un producto a la lista del restaurante
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Agrega un cliente a la lista del restaurante
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    # Muestra todos los productos registrados
    def mostrar_productos(self):
        print(f"\nProductos registrados en {self.nombre}:")
        if len(self.productos) == 0:
            print("No hay productos registrados.")
        else:
            for producto in self.productos:
                print(producto)

    # Muestra todos los clientes registrados
    def mostrar_clientes(self):
        print(f"\nClientes registrados en {self.nombre}:")
        if len(self.clientes) == 0:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente)    

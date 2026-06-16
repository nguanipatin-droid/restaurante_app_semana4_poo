from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear el restaurante principal
restaurante = Restaurante("Restaurante Sabor Andino")

# Crear productos del restaurante
producto_1 = Producto("Arroz con carne frita", "Plato fuerte", 3.50)
producto_2 = Producto("Jugo de mora", "Bebida", 1.25)
producto_3 = Producto("Empanada de queso", "Entrada", 1.00)

#Crear clientes del restaurante
cliente_1 = Cliente("Nahomy Guanipatin", "0991234567", 3)
cliente_2 = Cliente("Carlos Mera", "0987654321", 6)

# Agregar productos al restaurante
restaurante.agregar_producto(producto_1)
restaurante.agregar_producto(producto_2)
restaurante.agregar_producto(producto_3)

# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente_1)
restaurante.agregar_cliente(cliente_2)

# Mostrar la información registrada
restaurante.mostrar_productos()
restaurante.mostrar_clientes()
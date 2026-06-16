
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

restaurante = Restaurante("Restaurante Sabores del Ecuador")

producto1 = Producto("Hamburguesa", 6.50, "Comida")
producto2 = Producto("Pizza", 9.00, "Comida")
producto3 = Producto("Jugo de Naranja", 2.50, "Bebida")

cliente1 = Cliente("Steven", "0951234567", "0991112233")
cliente2 = Cliente("María", "0923456789", "0987654321")

restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

print("=" * 40)
print(restaurante.nombre)
print("=" * 40)

restaurante.mostrar_productos()
restaurante.mostrar_clientes()

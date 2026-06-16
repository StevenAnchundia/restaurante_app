
class Restaurante:

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\n===== PRODUCTOS =====")

        if len(self.productos) == 0:
            print("No existen productos registrados.")
        else:
            for producto in self.productos:
                print(producto)

    def mostrar_clientes(self):
        print("\n===== CLIENTES =====")

        if len(self.clientes) == 0:
            print("No existen clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente)

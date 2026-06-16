
class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} | Cedula: {self.cedula} | Telefono: {self.telefono}"

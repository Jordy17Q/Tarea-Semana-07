# Clase base
class DispositivoElectronico:
    def __init__(self, tipo, marca):
        self.tipo = tipo
        self.marca = marca
        print(f"[INICIO] Se ha creado un {self.tipo} de la marca {self.marca}.")

    def mostrar_info(self):
        print(f"Tipo: {self.tipo}, Marca: {self.marca}")

    def __del__(self):
        print(f"[FIN] Se ha eliminado el dispositivo {self.tipo} de la marca {self.marca}.")


# Clase derivada para Celulares
class Celular(DispositivoElectronico):
    def __init__(self, marca, sistema_operativo):
        super().__init__("Celular", marca)
        self.sistema_operativo = sistema_operativo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Sistema operativo: {self.sistema_operativo}")


# Clase derivada para Laptops
class Laptop(DispositivoElectronico):
    def __init__(self, marca, ram_gb, gpu_dedicada):
        super().__init__("Laptop", marca)
        self.ram_gb = ram_gb
        self.gpu_dedicada = gpu_dedicada

    def mostrar_info(self):
        super().mostrar_info()
        print(f"RAM: {self.ram_gb} GB")
        print(f"¿GPU dedicada?: {'Sí' if self.gpu_dedicada else 'No'}")


# Crear instancias
cel = Celular("Samsung", "Android")
cel.mostrar_info()

print("---")

lap = Laptop("Lenovo", 16, True)
lap.mostrar_info()

# Forzar eliminación (opcional en entornos interactivos)
del cel
del lap